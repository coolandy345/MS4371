Option Strict Off
Option Explicit On
Module GPIBGLOBAL
	'==========================================
	' Visual Basic Language Interface
	' Global valiables define
	' CONTEC Co.,Ltd.  2001.06.07
	'==========================================
	
	
	'--------------------
	' Global variables
	'--------------------
	Public ibsta As Short
	Public iberr As Short
	Public ibcnt As Short
	Public ibcntl(1) As Integer
	Public buf As String
	Public bytebuf() As Byte
	
	
	'--------------------
	' Needed to register for GPIB Global Thread.
	'--------------------
	Public Longibsta(1) As Integer
	Public Longiberr(1) As Integer
	Public Longibcnt(1) As Integer
	Public GPIBglobalsRegistered As Short
	
	
	'--------------------
	' Command defines
	'--------------------
	Public Const UNL As Short = &H3Fs
	Public Const UNT As Short = &H5Fs
	Public Const GTL As Short = &H1s
	Public Const SDC As Short = &H4s
	Public Const PPC As Short = &H5s
	Public Const GGET As Short = &H8s
	Public Const TCT As Short = &H9s
	Public Const LLO As Short = &H11s
	Public Const DCL As Short = &H14s
	Public Const PPU As Short = &H15s
	Public Const SPE As Short = &H18s
	Public Const SPD As Short = &H19s
	Public Const PPE As Short = &H60s
	Public Const PPD As Short = &H70s
	
	
	'--------------------
	' Status bit mask in ibsta
	'--------------------
	Public Const EERR As Short = &H8000s ' Error detected
	Public Const TIMO As Short = &H4000s ' Timeout occured
	Public Const EEND As Short = &H2000s ' EOI or EOS detected
	Public Const SRQI As Short = &H1000s ' SRQ detected by CIC
	Public Const RQS As Short = &H800s ' Device requesting any service
	Public Const CMPL As Short = &H100s ' I/O completed
	Public Const LOK As Short = &H80s ' Local lockout state
	Public Const RREM As Short = &H40s ' Remote enable state
	Public Const CIC As Short = &H20s ' Controller-in-Charge state
	Public Const AATN As Short = &H10s ' Attention line asserted state
	Public Const TACS As Short = &H8s ' Talker active state
	Public Const LACS As Short = &H4s ' Listener active state
	Public Const DTAS As Short = &H2s ' Device trigger state
	Public Const DCAS As Short = &H1s ' Device clear state
	
	
	'--------------------
	' Error messages in iberr
	'--------------------
	Public Const EDVR As Short = 0 ' System error
	Public Const ECIC As Short = 1 ' Function requires GPIB board to be CIC
	Public Const ENOL As Short = 2 ' Write function detected no Listeners
	Public Const EADR As Short = 3 ' Interface board not addressed correctly
	Public Const EARG As Short = 4 ' Invalid argument to function call
	Public Const ESAC As Short = 5 ' Function requires GPIB board to be SAC
	Public Const EABO As Short = 6 ' I/O operation aborted
	Public Const ENEB As Short = 7 ' Non-existent interface board
	Public Const EDMA As Short = 8 ' Error performing DMA
	Public Const EOIP As Short = 10 ' I/O operation started before previous operation completed
	Public Const ECAP As Short = 11 ' No capability for intended operation
	Public Const EFSO As Short = 12 ' File system operation error
	Public Const EBUS As Short = 14 ' Command error during device call
	Public Const ESTB As Short = 15 ' Serial poll status byte lost
	Public Const ESRQ As Short = 16 ' SRQ remains asserted
	Public Const ETAB As Short = 20 ' The return buffer is full
	Public Const ELCK As Short = 21 ' Address or board is locked
	
	
	'--------------------
	' EOS mode bits
	'--------------------
	Public Const BIN As Short = &H1000s ' EOS compare with eight bit
	Public Const XEOS As Short = &H800s ' Send EOI with EOS byte
	Public Const REOS As Short = &H400s ' Terminate read on EOS
	
	
	'--------------------
	' Timeout values and meanings
	'--------------------
	Public Const TNONE As Short = 0 ' Infinite timeout (disabled)
	Public Const T10us As Short = 1 ' Timeout of 10 uSec
	Public Const T30us As Short = 2 ' Timeout of 30 uSec
	Public Const T100us As Short = 3 ' Timeout of 100 uSec
	Public Const T300us As Short = 4 ' Timeout of 300 uSec
	Public Const T1ms As Short = 5 ' Timeout of 1 mSec
	Public Const T3ms As Short = 6 ' Timeout of 3 mSec
	Public Const T10ms As Short = 7 ' Timeout of 10 mSec
	Public Const T30ms As Short = 8 ' Timeout of 30 mSec
	Public Const T100ms As Short = 9 ' Timeout of 100 mSec
	Public Const T300ms As Short = 10 ' Timeout of 300 mSec
	Public Const T1s As Short = 11 ' Timeout of 1 Sec
	Public Const T3s As Short = 12 ' Timeout of 3 Sec
	Public Const T10s As Short = 13 ' Timeout of 10 Sec
	Public Const T30s As Short = 14 ' Timeout of 30 Sec
	Public Const T100s As Short = 15 ' Timeout of 100 Sec
	Public Const T300s As Short = 16 ' Timeout of 300 Sec
	Public Const T1000s As Short = 17 ' Timeout of 1000 Sec
	
	
	'--------------------
	' Secondary address setting
	'--------------------
	Public Const ALL_SAD As Short = -1 ' No Secondary address use
	Public Const NO_SAD As Short = 0 ' All Secondary address check
	
	
	'--------------------
	' ibconfig parameter defines
	'--------------------
	Public Const IbcPAD As Short = &H1s ' Primary Address setting
	Public Const IbcSAD As Short = &H2s ' Secondary Address setting
	Public Const IbcTMO As Short = &H3s ' Timeout Value setting
	Public Const IbcEOT As Short = &H4s ' Send EOI with last data byte setting
	Public Const IbcPPC As Short = &H5s ' Parallel Poll Configure setting
	Public Const IbcREADDR As Short = &H6s ' Repeat Addressing setting
	Public Const IbcAUTOPOLL As Short = &H7s ' Disable Auto Serial Polling setting
	Public Const IbcCICPROT As Short = &H8s ' Use the CIC Protocol setting (Not supported by CONTEC)
	Public Const IbcIRQ As Short = &H9s ' Use PIO for I/O setting (Not supported by CONTEC)
	Public Const IbcSC As Short = &HAs ' System Controller setting
	Public Const IbcSRE As Short = &HBs ' Assert SRE on device calls setting
	Public Const IbcEOSrd As Short = &HCs ' Terminate reads on EOS setting
	Public Const IbcEOSwrt As Short = &HDs ' Send EOI with EOS character setting
	Public Const IbcEOScmp As Short = &HEs ' Use 7 or 8-bit EOS compare setting
	Public Const IbcEOSchar As Short = &HFs ' The EOS character setting
	Public Const IbcPP2 As Short = &H10s ' Use Parallel Poll Mode 2 setting
	Public Const IbcTIMING As Short = &H11s ' NORMAL, HIGH, or VERY_HIGH timing setting
	Public Const IbcDMA As Short = &H12s ' Use DMA for I/O setting
	Public Const IbcReadAdjust As Short = &H13s ' Swap bytes during an ibrd setting
	Public Const IbcWriteAdjust As Short = &H14s ' Swap bytes during an ibwrt setting
	Public Const IbcSendLLO As Short = &H17s ' Enable/disable the sending of LLO setting
	Public Const IbcSPollTime As Short = &H18s ' Set the timeout value for serial polls setting
	Public Const IbcPPollTime As Short = &H19s ' Set the parallel poll length period setting
	Public Const IbcEndBitIsNormal As Short = &H1As ' Remove EOS from END bit of IBSTA setting
	Public Const IbcUnAddr As Short = &H1Bs ' Enable/disable device unaddressing setting
	Public Const IbcHSCableLength As Short = &H1Fs ' Enable/disable high-speed handshaking setting (Not supported by CONTEC)
	Public Const IbcIst As Short = &H20s ' Set the IST bit setting
	Public Const IbcRsv As Short = &H21s ' Set the RSV bit setting
	
	
	'--------------------
	' ibask parameter defines
	'--------------------
	Public Const IbaPAD As Short = &H1s ' Primary Address setting
	Public Const IbaSAD As Short = &H2s ' Secondary Address setting
	Public Const IbaTMO As Short = &H3s ' Timeout Value setting
	Public Const IbaEOT As Short = &H4s ' Send EOI with last data byte? setting
	Public Const IbaPPC As Short = &H5s ' Parallel Poll Configure setting
	Public Const IbaREADDR As Short = &H6s ' Repeat Addressing setting
	Public Const IbaAUTOPOLL As Short = &H7s ' Disable Auto Serial Polling setting
	Public Const IbaCICPROT As Short = &H8s ' Use the CIC Protocol setting (Not supported by CONTEC)
	Public Const IbaIRQ As Short = &H9s ' Use PIO for I/O setting (Not supported by CONTEC)
	Public Const IbaSC As Short = &HAs ' System Controller setting
	Public Const IbaSRE As Short = &HBs ' Assert SRE on device calls setting
	Public Const IbaEOSrd As Short = &HCs ' Terminate reads on EOS setting
	Public Const IbaEOSwrt As Short = &HDs ' Send EOI with EOS character setting
	Public Const IbaEOScmp As Short = &HEs ' Use 7 or 8-bit EOS compare setting
	Public Const IbaEOSchar As Short = &HFs ' The EOS character setting
	Public Const IbaPP2 As Short = &H10s ' Use Parallel Poll Mode 2 setting
	Public Const IbaTIMING As Short = &H11s ' NORMAL, HIGH, or VERY_HIGH timing setting
	Public Const IbaDMA As Short = &H12s ' Use DMA for I/O setting
	Public Const IbaReadAdjust As Short = &H13s ' Swap bytes during an ibrd setting
	Public Const IbaWriteAdjust As Short = &H14s ' Swap bytes during an ibwrt setting
	Public Const IbaSendLLO As Short = &H17s ' Enable/disable the sending of LLO setting
	Public Const IbaSPollTime As Short = &H18s ' Set the timeout value for serial polls setting
	Public Const IbaPPollTime As Short = &H19s ' Set the parallel poll length period setting
	Public Const IbaEndBitIsNormal As Short = &H1As ' Remove EOS from END bit of ibsta setting
	Public Const IbaUnAddr As Short = &H1Bs ' Enable/disable device unaddressing setting
	Public Const IbaHSCableLength As Short = &H1Fs ' Enable/disable high-speed handshaking setting (Not supported by CONTEC)
	Public Const IbaIst As Short = &H20s ' Set the IST bit setting
	Public Const IbaRsv As Short = &H21s ' Set the RSV bit setting
	Public Const IbaBNA As Short = &H200s ' A device's access board setting
	
	
	'--------------------
	' iblines parameter defines
	'--------------------
	Public Const ValidEOI As Short = &H80s
	Public Const ValidATN As Short = &H40s
	Public Const ValidSRQ As Short = &H20s
	Public Const ValidREN As Short = &H10s
	Public Const ValidIFC As Short = &H8s
	Public Const ValidNRFD As Short = &H4s
	Public Const ValidNDAC As Short = &H2s
	Public Const ValidDAV As Short = &H1s
	Public Const BusEOI As Short = &H8000s
	Public Const BusATN As Short = &H4000s
	Public Const BusSRQ As Short = &H2000s
	Public Const BusREN As Short = &H1000s
	Public Const BusIFC As Short = &H800s
	Public Const BusNRFD As Short = &H400s
	Public Const BusNDAC As Short = &H200s
	Public Const BusDAV As Short = &H100s
	
	
	'--------------------
	' iblines parameter defines
	'--------------------
	Public Const NULLend As Short = &H0s ' Do nothing at the end of a transfer
	Public Const NLend As Short = &H1s ' Send NL with EOI after a transfer
	Public Const DABend As Short = &H2s ' Send EOI with the last DAB
	
	
	'--------------------
	' Values used by the 488.2 Receive command
	'--------------------
	Public Const STOPend As Short = &H100s ' Stop the read on EOI
	
	'--------------------
	' NOADDR define
	'--------------------
	Public Const NOADDR As Short = &HFFFFs
	
	
	'--------------------
	' ibnotify error code
	'--------------------
	Public Const IBNOTIFY_REARM_FAILED As Integer = &HE00A003F
End Module