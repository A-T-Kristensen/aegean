def writeHeader(f):
    f.write('''\
--------------------------------------------------------------------------------
-- Auto generated entity for the aegean platform,
-- processors, communication scratch pads and network on chip.
--------------------------------------------------------------------------------
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

use work.config.all;
use work.ocp.all;
use work.noc_interface.all;

entity aegean is
    port(
        clk   : in  std_logic;
        reset : in std_logic;
        led   : out std_logic_vector(8 downto 0);
        txd   : out std_logic;
        rxd   : in  std_logic;

        -- Sram signals
        io_sramPins_ram_out_addr    : out std_logic_vector(18 downto 0);
        io_sramPins_ram_out_dout_ena: out std_logic;
        io_sramPins_ram_out_nadsc   : out std_logic;
        io_sramPins_ram_out_noe     : out std_logic;
        io_sramPins_ram_out_nbwe    : out std_logic;
        io_sramPins_ram_out_nbw     : out std_logic_vector(3 downto 0);
        io_sramPins_ram_out_ngw     : out std_logic;
        io_sramPins_ram_out_nce1    : out std_logic;
        io_sramPins_ram_out_ce2     : out std_logic;
        io_sramPins_ram_out_nce3    : out std_logic;
        io_sramPins_ram_out_nadsp   : out std_logic;
        io_sramPins_ram_out_nadv    : out std_logic;
        io_sramPins_ram_out_dout    : out std_logic_vector(31 downto 0);
        io_sramPins_ram_in_din      : in  std_logic_vector(31 downto 0)
    );
end entity ; -- aegean

architecture struct of aegean is
    component SsramBurstRW is
    port (
        clk                       :   in  std_logic;
        reset                     :   in  std_logic;
        io_ocp_port_M_Cmd         :   in  std_logic_vector(2 downto 0);
        io_ocp_port_M_Addr        :   in  std_logic_vector(20 downto 0);
        io_ocp_port_M_Data        :   in  std_logic_vector(31 downto 0);
        io_ocp_port_M_DataValid   :   in  std_logic;
        io_ocp_port_M_DataByteEn  :   in  std_logic_vector(3 downto 0);
        io_ocp_port_S_Resp        :   out std_logic_vector(1 downto 0);
        io_ocp_port_S_Data        :   out std_logic_vector(31 downto 0);
        io_ocp_port_S_CmdAccept   :   out std_logic;
        io_ocp_port_S_DataAccept  :   out std_logic;
        io_ram_out_addr           :   out std_logic_vector(18 downto 0);
        io_ram_out_dout_ena       :   out std_logic;
        io_ram_out_nadsc          :   out std_logic;
        io_ram_out_noe            :   out std_logic;
        io_ram_out_nbwe           :   out std_logic;
        io_ram_out_nbw            :   out std_logic_vector(3 downto 0);
        io_ram_out_ngw            :   out std_logic;
        io_ram_out_nce1           :   out std_logic;
        io_ram_out_ce2            :   out std_logic;
        io_ram_out_nce3           :   out std_logic;
        io_ram_out_nadsp          :   out std_logic;
        io_ram_out_nadv           :   out std_logic;
        io_ram_out_dout           :   out std_logic_vector(31 downto 0);
        io_ram_in_din             :   in  std_logic_vector(31 downto 0)
        );
    end component;

    component Arbiter is
    port (
        clk                   : in std_logic;
        reset                 : in std_logic;

        io_slave_M_Cmd        : out std_logic_vector(2 downto 0);
        io_slave_M_Addr       : out std_logic_vector(20 downto 0);
        io_slave_M_Data       : out std_logic_vector(31 downto 0);
        io_slave_M_DataValid  : out std_logic;
        io_slave_M_DataByteEn : out std_logic_vector(3 downto 0);
        io_slave_S_Resp       : in  std_logic_vector(1 downto 0);
        io_slave_S_Data       : in  std_logic_vector(31 downto 0);
        io_slave_S_CmdAccept  : in  std_logic;
        io_slave_S_DataAccept : in  std_logic;
''')

def writeArbiterCompPort(f,i):
    f.write('''
        io_master_'''+str(i)+'''_M_Cmd        : in std_logic_vector(2 downto 0);
        io_master_'''+str(i)+'''_M_Addr       : in std_logic_vector(20 downto 0);
        io_master_'''+str(i)+'''_M_Data       : in std_logic_vector(31 downto 0);
        io_master_'''+str(i)+'''_M_DataValid  : in std_logic;
        io_master_'''+str(i)+'''_M_DataByteEn : in std_logic_vector(3 downto 0);
        io_master_'''+str(i)+'''_S_Resp       : out std_logic_vector(1 downto 0);
        io_master_'''+str(i)+'''_S_Data       : out std_logic_vector(31 downto 0);
        io_master_'''+str(i)+'''_S_CmdAccept  : out std_logic;
        io_master_'''+str(i)+'''_S_DataAccept : out std_logic''')

def writeArbiterCompEnd(f):
    f.write('''
        );
    end component;
''')

def writePatmosComp(f,IPType):
    f.write('''
    component '''+IPType+'''PatmosCore is
    port(
        clk                         : in  std_logic;
        reset                       : in  std_logic;
        io_cpuId                    : in  std_logic_vector(31 downto 0);
        -- Communication scratch pad signals
        io_comConf_M_Cmd            : out std_logic_vector(2 downto 0);
        io_comConf_M_Addr           : out std_logic_vector(31 downto 0);
        io_comConf_M_Data           : out std_logic_vector(31 downto 0);
        io_comConf_M_ByteEn         : out std_logic_vector(3 downto 0);
        io_comConf_M_RespAccept     : out std_logic;
        io_comConf_S_Resp           : in  std_logic_vector(1 downto 0);
        io_comConf_S_Data           : in  std_logic_vector(31 downto 0);
        io_comConf_S_CmdAccept      : in  std_logic;
        io_comSpm_M_Cmd             : out std_logic_vector(2 downto 0);
        io_comSpm_M_Addr            : out std_logic_vector(31 downto 0);
        io_comSpm_M_Data            : out std_logic_vector(31 downto 0);
        io_comSpm_M_ByteEn          : out std_logic_vector(3 downto 0);
        io_comSpm_S_Resp            : in  std_logic_vector(1 downto 0);
        io_comSpm_S_Data            : in  std_logic_vector(31 downto 0);
        -- Simple IO signals
        io_led                      : out std_logic_vector(8 downto 0);
        io_uartPins_tx              : out std_logic;
        io_uartPins_rx              : in  std_logic;
        -- Memory port signals
        io_memPort_M_Cmd            : out std_logic_vector(2 downto 0);
        io_memPort_M_Addr           : out std_logic_vector(20 downto 0);
        io_memPort_M_Data           : out std_logic_vector(31 downto 0);
        io_memPort_M_DataValid      : out std_logic;
        io_memPort_M_DataByteEn     : out std_logic_vector(3 downto 0);
        io_memPort_S_Resp           : in  std_logic_vector(1 downto 0);
        io_memPort_S_Data           : in  std_logic_vector(31 downto 0);
        io_memPort_S_CmdAccept      : in  std_logic;
        io_memPort_S_DataAccept     : in  std_logic
        );
    end component;
''')

def writeSignals(f):
    f.write('''
    signal ocp_io_ms : ocp_io_m_a;
    signal ocp_io_ss : ocp_io_s_a;


    signal ocp_core_ms : ocp_core_m_a;
    signal ocp_core_ss : ocp_core_s_a;

    signal ocp_burst_ms : ocp_burst_m_a;
    signal ocp_burst_ss : ocp_burst_s_a;

    signal ocp_burst_m_mem : ocp_burst_m;
    signal ocp_burst_s_mem : ocp_burst_s;

    signal spm_ms : spm_masters;
    signal spm_ss : spm_slaves;


begin
''')

def writePatmosInst(f,label,IPType,p,ledPort,txdPort,rxdPort):
    f.write('''
    '''+label+''' : '''+IPType+'''PatmosCore port map(
        clk                           => clk,
        reset                         => reset,
        io_cpuId                      => std_logic_vector(to_unsigned('''+str(p)+''',32)),
        io_comConf_M_Cmd              => ocp_io_ms('''+str(p)+''').MCmd,
        io_comConf_M_Addr             => ocp_io_ms('''+str(p)+''').MAddr,
        io_comConf_M_Data             => ocp_io_ms('''+str(p)+''').MData,
        io_comConf_M_ByteEn           => ocp_io_ms('''+str(p)+''').MByteEn,
        io_comConf_M_RespAccept       => ocp_io_ms('''+str(p)+''').MRespAccept,
        io_comConf_S_Resp             => ocp_io_ss('''+str(p)+''').SResp,
        io_comConf_S_Data             => ocp_io_ss('''+str(p)+''').SData,
        io_comConf_S_CmdAccept        => ocp_io_ss('''+str(p)+''').SCmdAccept,
        io_comSpm_M_Cmd               => ocp_core_ms('''+str(p)+''').MCmd,
        io_comSpm_M_Addr              => ocp_core_ms('''+str(p)+''').MAddr,
        io_comSpm_M_Data              => ocp_core_ms('''+str(p)+''').MData,
        io_comSpm_M_ByteEn            => ocp_core_ms('''+str(p)+''').MByteEn,
        io_comSpm_S_Resp              => ocp_core_ss('''+str(p)+''').SResp,
        io_comSpm_S_Data              => ocp_core_ss('''+str(p)+''').SData,
        io_led                        => '''+ledPort+''',
        io_uartPins_tx                => '''+txdPort+''',
        io_uartPins_rx                => '''+rxdPort+''',
        io_memPort_M_Cmd              => ocp_burst_ms('''+str(p)+''').MCmd,
        io_memPort_M_Addr             => ocp_burst_ms('''+str(p)+''').MAddr,
        io_memPort_M_Data             => ocp_burst_ms('''+str(p)+''').MData,
        io_memPort_M_DataValid        => ocp_burst_ms('''+str(p)+''').MDataValid,
        io_memPort_M_DataByteEn       => ocp_burst_ms('''+str(p)+''').MDataByteEn,
        io_memPort_S_Resp             => ocp_burst_ss('''+str(p)+''').SResp,
        io_memPort_S_Data             => ocp_burst_ss('''+str(p)+''').SData,
        io_memPort_S_CmdAccept        => ocp_burst_ss('''+str(p)+''').SCmdAccept,
        io_memPort_S_DataAccept       => ocp_burst_ss('''+str(p)+''').SDataAccept
    );

''')

def writeInterconnect(f):
    f.write('''\

    spms : for i in 0 to NODES-1 generate
        spm : entity work.com_spm port map(
            p_clk => clk,
            n_clk => clk,
            reset => reset,
            ocp_core_m => ocp_core_ms(i),
            ocp_core_s => ocp_core_ss(i),
            spm_m => spm_ms(i),
            spm_s => spm_ss(i)
            );
    end generate ; -- spms

    noc : entity work.noc port map(
        clk => clk,
        reset => reset,
        ocp_io_ms => ocp_io_ms,
        ocp_io_ss => ocp_io_ss,
        spm_ports_m => spm_ms,
        spm_ports_s => spm_ss
    );

    ssram : SsramBurstRW port map(
        clk                       => clk,
        reset                     => reset,
        io_ocp_port_M_Cmd         => ocp_burst_m_mem.MCmd,
        io_ocp_port_M_Addr        => ocp_burst_m_mem.MAddr(20 downto 0),
        io_ocp_port_M_Data        => ocp_burst_m_mem.MData,
        io_ocp_port_M_DataValid   => ocp_burst_m_mem.MDataValid,
        io_ocp_port_M_DataByteEn  => ocp_burst_m_mem.MDataByteEn,
        io_ocp_port_S_Resp        => ocp_burst_s_mem.SResp,
        io_ocp_port_S_Data        => ocp_burst_s_mem.SData,
        io_ocp_port_S_CmdAccept   => ocp_burst_s_mem.SCmdAccept,
        io_ocp_port_S_DataAccept  => ocp_burst_s_mem.SDataAccept,
        io_ram_out_addr           => io_sramPins_ram_out_addr    ,
        io_ram_out_dout_ena       => io_sramPins_ram_out_dout_ena,
        io_ram_out_nadsc          => io_sramPins_ram_out_nadsc   ,
        io_ram_out_noe            => io_sramPins_ram_out_noe     ,
        io_ram_out_nbwe           => io_sramPins_ram_out_nbwe    ,
        io_ram_out_nbw            => io_sramPins_ram_out_nbw     ,
        io_ram_out_ngw            => io_sramPins_ram_out_ngw     ,
        io_ram_out_nce1           => io_sramPins_ram_out_nce1    ,
        io_ram_out_ce2            => io_sramPins_ram_out_ce2     ,
        io_ram_out_nce3           => io_sramPins_ram_out_nce3    ,
        io_ram_out_nadsp          => io_sramPins_ram_out_nadsp   ,
        io_ram_out_nadv           => io_sramPins_ram_out_nadv    ,
        io_ram_out_dout           => io_sramPins_ram_out_dout    ,
        io_ram_in_din             => io_sramPins_ram_in_din
    );

    arbit : Arbiter port map(
        clk                       => clk,
        reset                     => reset,

        io_slave_M_Cmd            => ocp_burst_m_mem.MCmd,
        io_slave_M_Addr           => ocp_burst_m_mem.MAddr(20 downto 0),
        io_slave_M_Data           => ocp_burst_m_mem.MData,
        io_slave_M_DataValid      => ocp_burst_m_mem.MDataValid,
        io_slave_M_DataByteEn     => ocp_burst_m_mem.MDataByteEn,
        io_slave_S_Resp           => ocp_burst_s_mem.SResp,
        io_slave_S_Data           => ocp_burst_s_mem.SData,
        io_slave_S_CmdAccept      => ocp_burst_s_mem.SCmdAccept,
        io_slave_S_DataAccept     => ocp_burst_s_mem.SDataAccept,
''')

def writeArbiterInstPort(f,i):
    f.write('''
        io_master_'''+str(i)+'''_M_Cmd        => ocp_burst_ms('''+str(i)+''').MCmd,
        io_master_'''+str(i)+'''_M_Addr       => ocp_burst_ms('''+str(i)+''').MAddr,
        io_master_'''+str(i)+'''_M_Data       => ocp_burst_ms('''+str(i)+''').MData,
        io_master_'''+str(i)+'''_M_DataValid  => ocp_burst_ms('''+str(i)+''').MDataValid,
        io_master_'''+str(i)+'''_M_DataByteEn => ocp_burst_ms('''+str(i)+''').MDataByteEn,
        io_master_'''+str(i)+'''_S_Resp       => ocp_burst_ss('''+str(i)+''').SResp,
        io_master_'''+str(i)+'''_S_Data       => ocp_burst_ss('''+str(i)+''').SData,
        io_master_'''+str(i)+'''_S_CmdAccept  => ocp_burst_ss('''+str(i)+''').SCmdAccept,
        io_master_'''+str(i)+'''_S_DataAccept => ocp_burst_ss('''+str(i)+''').SDataAccept''')

def writeFooter(f):
    f.write('''
    );

end architecture ; -- struct

''')
