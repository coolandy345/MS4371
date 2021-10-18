/*=============================================

	For C/C++ Function & Variable Declations
	CONTEC Co.,Ltd.	 2001.06.07

=============================================*/

#ifndef	__GPCMDECL_H__
#define	__GPCMDECL_H__

#ifdef __cplusplus
extern "C" {
#endif

//--------------------
// Command defines
//--------------------
#define	UNL			0x3f
#define	UNT			0x5f
#define	GTL			0x01
#define	SDC			0x04
#define	PPC			0x05
#define	GET			0x08
#define	TCT			0x09
#define	LLO			0x11
#define	DCL			0x14
#define	PPU			0x15
#define	SPE			0x18
#define	SPD			0x19
#define	PPE			0x60
#define	PPD			0x70


//--------------------
// Status bit mask in ibsta
//--------------------
#define	ERR			0x8000	// Error detected
#define	TIMO		0x4000	// Timeout occured
#define	END			0x2000	// EOI or EOS detected
#define	SRQI		0x1000	// SRQ detected by CIC
#define	RQS			0x0800	// Device requested any service
#define	CMPL		0x0100	// I/O completed
#define	LOK			0x0080	// Local lockout state
#define	REM			0x0040	// Remote enable state
#define	CIC			0x0020	// Controller-in-Charge state
#define	ATN			0x0010	// Attention line asserted
#define	TACS		0x0008	// Talker active state
#define	LACS		0x0004	// Listener active state
#define	DTAS		0x0002	// Device trigger state
#define	DCAS		0x0001	// Device clear state


//--------------------
// Error messages in iberr
//--------------------
#define	EDVR		 0		// System error
#define	ECIC		 1		// Function requires GPIB board to be CIC
#define	ENOL		 2		// Write function detected no Listeners
#define	EADR		 3		// Interface board not addressed correctly
#define	EARG		 4		// Invalid argument to function call
#define	ESAC		 5		// Function requires GPIB board to be SAC
#define	EABO		 6		// I/O operation aborted
#define	ENEB		 7		// Non-existent interface board
#define	EDMA		 8		// Error performing DMA
#define	EOIP		10		// I/O operation started before previous operation completed
#define	ECAP		11		// No capability for intended operation
#define	EFSO		12		// File system operation error
#define	EBUS		14		// Command error during device call
#define	ESTB		15		// Serial poll status byte lost
#define	ESRQ		16		// SRQ remains asserted
#define	ETAB		20		// The return buffer is full
#define	ELCK		21		// Address or board is locked


//--------------------
// EOS mode bits
//--------------------
#define	BIN			0x1000	// EOS compare with eight bit
#define	XEOS		0x0800	// Send END with EOS byte
#define	REOS		0x0400	// Terminate read on EOS


//--------------------
// Timeout values and meanings
//--------------------
#define	TNONE		 0		// Infinite timeout (disabled)
#define	T10us		 1		// Timeout of 10 uSec
#define	T30us		 2		// Timeout of 30 uSec
#define	T100us		 3		// Timeout of 100 uSec
#define	T300us		 4		// Timeout of 300 uSec
#define	T1ms		 5		// Timeout of 1 mSec
#define	T3ms		 6		// Timeout of 3 mSec
#define	T10ms		 7		// Timeout of 10 mSec
#define	T30ms		 8		// Timeout of 30 mSec
#define	T100ms		 9		// Timeout of 100 mSec
#define	T300ms		10		// Timeout of 300 mSec
#define	T1s			11		// Timeout of 1 Sec
#define	T3s			12		// Timeout of 3 Sec
#define	T10s		13		// Timeout of 10 Sec
#define	T30s		14		// Timeout of 30 Sec
#define	T100s		15		// Timeout of 100 Sec
#define	T300s		16		// Timeout of 300 Sec
#define	T1000s		17		// Timeout of 1000 Sec


//--------------------
// Secondary address setting
//--------------------
#define	NO_SAD		 0		// No Secondary address use
#define	ALL_SAD		-1		// All Secondary address check


//--------------------
// ibconfig parameter defines
//--------------------
#define	IbcPAD				0x0001		// Primary Address setting
#define	IbcSAD				0x0002		// Secondary Address setting
#define	IbcTMO				0x0003		// Timeout Value setting
#define	IbcEOT				0x0004		// Send EOI with last data byte  setting
#define	IbcPPC				0x0005		// Parallel Poll Configure setting
#define	IbcREADDR			0x0006		// Repeat Addressing setting
#define	IbcAUTOPOLL			0x0007		// Auto Serial Polling setting
#define	IbcCICPROT			0x0008		// Use the CIC Protocol setting (Not supported by CONTEC)
#define	IbcIRQ				0x0009		// Use PIO for I/O setting (Not supported by CONTEC)
#define	IbcSC				0x000A		// System Controller setting
#define	IbcSRE				0x000B		// Assert REN on device calls setting
#define	IbcEOSrd			0x000C		// Terminate reads on EOS setting
#define	IbcEOSwrt			0x000D		// Send EOI with EOS character setting
#define	IbcEOScmp			0x000E		// Use 7 or 8-bit EOS compare setting
#define	IbcEOSchar			0x000F		// The EOS character setting
#define	IbcPP2				0x0010		// Use Parallel Poll Mode 2 setting
#define	IbcTIMING			0x0011		// NORMAL, HIGH, or VERY_HIGH timing setting
#define	IbcDMA				0x0012		// Use DMA for I/O setting
#define	IbcReadAdjust		0x0013		// Swap bytes during an ibrd setting
#define	IbcWriteAdjust		0x0014		// Swap bytes during an ibwrt setting
#define	IbcSendLLO			0x0017		// Enable/disable the sending of LLO setting
#define	IbcSPollTime		0x0018		// Set the timeout value for serial polls setting
#define	IbcPPollTime		0x0019		// Set the parallel poll length period setting
#define	IbcEndBitIsNormal	0x001A		// Remove EOS from END bit of ibsta setting
#define	IbcUnAddr			0x001B		// Enable/disable device unaddressing setting
#define	IbcHSCableLength	0x001F		// Length of cable specified for high speed timing setting (Not supported by CONTEC)
#define	IbcIst				0x0020		// Set the IST bit setting
#define	IbcRsv				0x0021		// Set the RSV byte setting


//--------------------
// ibask parameter defines
//--------------------
#define	IbaPAD				IbcPAD
#define	IbaSAD				IbcSAD
#define	IbaTMO				IbcTMO
#define	IbaEOT				IbcEOT
#define	IbaPPC				IbcPPC
#define	IbaREADDR			IbcREADDR
#define	IbaAUTOPOLL			IbcAUTOPOLL
#define	IbaCICPROT			IbcCICPROT
#define	IbaIRQ				IbcIRQ
#define	IbaSC				IbcSC
#define	IbaSRE				IbcSRE
#define	IbaEOSrd			IbcEOSrd
#define	IbaEOSwrt			IbcEOSwrt
#define	IbaEOScmp			IbcEOScmp
#define	IbaEOSchar			IbcEOSchar
#define	IbaPP2				IbcPP2
#define	IbaTIMING			IbcTIMING
#define	IbaDMA				IbcDMA
#define	IbaReadAdjust		IbcReadAdjust
#define	IbaWriteAdjust		IbcWriteAdjust
#define	IbaSendLLO			IbcSendLLO
#define	IbaSPollTime		IbcSPollTime
#define	IbaPPollTime		IbcPPollTime
#define	IbaEndBitIsNormal	IbcEndBitIsNormal
#define	IbaUnAddr			IbcUnAddr
#define	IbaHSCableLength	IbcHSCableLength
#define	IbaIst				IbcIst
#define	IbaRsv				IbcRsv
#define	IbaBNA				0x0200		// A device's access board setting


//--------------------
// iblines parameter defines
//--------------------
#define	ValidEOI	(short)0x0080
#define	ValidATN	(short)0x0040
#define	ValidSRQ	(short)0x0020
#define	ValidREN	(short)0x0010
#define	ValidIFC	(short)0x0008
#define	ValidNRFD	(short)0x0004
#define	ValidNDAC	(short)0x0002
#define	ValidDAV	(short)0x0001
#define	BusEOI		(short)0x8000
#define	BusATN		(short)0x4000
#define	BusSRQ		(short)0x2000
#define	BusREN		(short)0x1000
#define	BusIFC		(short)0x0800
#define	BusNRFD		(short)0x0400
#define	BusNDAC		(short)0x0200
#define	BusDAV		(short)0x0100


//--------------------
// Values used by the 488.2 Send command
//--------------------
#define	NULLend		0x00	// Do nothing at the end of a transfer
#define	NLend		0x01	// Send NL with EOI after a transfer
#define	DABend		0x02	// Send EOI with the last DAB


//--------------------
// Values used by the 488.2 Receive command
//--------------------
#define	STOPend		0x0100	// Receive stop by EOS recognized


//--------------------
// Address type define
//--------------------
typedef short Addr4882_t;	// Must be 16 bits


//--------------------
// NOADDR define
//--------------------
#ifndef	NOADDR
#define	NOADDR		(Addr4882_t)((unsigned short)0xffff)
#endif


//--------------------
// Make "Addr4882_t" type from pad and sad
//--------------------
#define	MakeAddr(pad, sad)	((Addr4882_t)(((pad) & 0xff) | ((sad) << 8)))


//--------------------
// Extract pad or sad from "Addr4882_t" type parameter
//--------------------
#define	GetPAD(val)	((val) & 0xff)
#define	GetSAD(val)	(((val) >> 8) & 0xff)


//--------------------
// typedef for ibnotify callback
//--------------------
typedef int (__stdcall * GpibNotifyCallback_t)(int, int, int, long, PVOID);
#define IBNOTIFY_REARM_FAILED    0xE00A003F



#if !defined(GPIB_DIRECT_ACCESS)
//--------------------
// Global valiables define
//--------------------
#define	ibsta	(ThreadIbsta())
#define	iberr	(ThreadIberr())
#define	ibcnt	(ThreadIbcnt())
#define	ibcntl	(ThreadIbcntl())

//--------------------
// Function prototypes
//--------------------
#if defined(UNICODE)
   #define ibbna  ibbnaW
   #define ibfind ibfindW
   #define ibrdf  ibrdfW
   #define ibwrtf ibwrtfW
#else
   #define ibbna  ibbnaA
   #define ibfind ibfindA
   #define ibrdf  ibrdfA
   #define ibwrtf ibwrtfA
#endif

extern int __stdcall ibfindA		(LPCSTR udname);
extern int __stdcall ibbnaA			(int ud, LPCSTR udname);
extern int __stdcall ibrdfA			(int ud, LPCSTR filename);
extern int __stdcall ibwrtfA		(int ud, LPCSTR filename);
extern int __stdcall ibfindW		(LPCWSTR udname);
extern int __stdcall ibbnaW			(int ud, LPCWSTR udname);
extern int __stdcall ibrdfW			(int ud, LPCWSTR filename);
extern int __stdcall ibwrtfW		(int ud, LPCWSTR filename);
extern int __stdcall ibask			(int ud, int option, PINT v);
extern int __stdcall ibcac			(int ud, int v);
extern int __stdcall ibclr			(int ud);
extern int __stdcall ibcmd			(int ud, PVOID buf, long cnt);
extern int __stdcall ibcmda			(int ud, PVOID buf, long cnt);
extern int __stdcall ibconfig		(int ud, int option, int v);
extern int __stdcall ibdev			(int boardID, int pad, int sad, int tmo, int eot, int eos);
extern int __stdcall ibdma			(int ud, int v);
extern int __stdcall ibeos			(int ud, int v);
extern int __stdcall ibeot			(int ud, int v);
extern int __stdcall ibgts			(int ud, int v);
extern int __stdcall ibist			(int ud, int v);
extern int __stdcall iblines		(int ud, PSHORT result);
extern int __stdcall ibln			(int ud, int pad, int sad, PSHORT listen);
extern int __stdcall ibloc			(int ud);
extern int __stdcall ibnotify		(int ud, int mask, GpibNotifyCallback_t Callback, PVOID RefData);
extern int __stdcall ibonl			(int ud, int v);
extern int __stdcall ibpad			(int ud, int v);
extern int __stdcall ibpct			(int ud);
extern int __stdcall ibppc			(int ud, int v);
extern int __stdcall ibrd			(int ud, PVOID buf, long cnt);
extern int __stdcall ibrda			(int ud, PVOID buf, long cnt);
extern int __stdcall ibrpp			(int ud, PCHAR ppr);
extern int __stdcall ibrsc			(int ud, int v);
extern int __stdcall ibrsp			(int ud, PCHAR spr);
extern int __stdcall ibrsv			(int ud, int v);
extern int __stdcall ibsad			(int ud, int v);
extern int __stdcall ibsic			(int ud);
extern int __stdcall ibsre			(int ud, int v);
extern int __stdcall ibstop			(int ud);
extern int __stdcall ibtmo			(int ud, int v);
extern int __stdcall ibtrg			(int ud);
extern int __stdcall ibwait			(int ud, int mask);
extern int __stdcall ibwrt			(int ud, PVOID buf, long cnt);
extern int __stdcall ibwrta			(int ud, PVOID buf, long cnt);

extern int  __stdcall ThreadIbsta	(void);
extern int  __stdcall ThreadIberr	(void);
extern int  __stdcall ThreadIbcnt	(void);
extern long __stdcall ThreadIbcntl	(void);

extern void __stdcall AllSpoll		(int boardID, Addr4882_t * addrlist, PSHORT results);
extern void __stdcall DevClear		(int boardID, Addr4882_t addr);
extern void __stdcall DevClearList	(int boardID, Addr4882_t * addrlist);
extern void __stdcall EnableLocal	(int boardID, Addr4882_t * addrlist);
extern void __stdcall EnableRemote	(int boardID, Addr4882_t * addrlist);
extern void __stdcall FindLstn		(int boardID, Addr4882_t * addrlist, Addr4882_t * results, int limit);
extern void __stdcall FindRQS		(int boardID, Addr4882_t * addrlist, PSHORT dev_stat);
extern void __stdcall PPoll			(int boardID, PSHORT result);
extern void __stdcall PPollConfig	(int boardID, Addr4882_t addr, int dataLine, int lineSense);
extern void __stdcall PPollUnconfig	(int boardID, Addr4882_t * addrlist);
extern void __stdcall PassControl	(int boardID, Addr4882_t addr);
extern void __stdcall RcvRespMsg	(int boardID, PVOID buffer, long cnt, int Termination);
extern void __stdcall ReadStatusByte(int boardID, Addr4882_t addr, PSHORT result);
extern void __stdcall Receive		(int boardID, Addr4882_t addr, PVOID buffer, long cnt, int Termination);
extern void __stdcall ReceiveSetup	(int boardID, Addr4882_t addr);
extern void __stdcall ResetSys		(int boardID, Addr4882_t * addrlist);
extern void __stdcall Send			(int boardID, Addr4882_t addr, PVOID databuf, long datacnt, int eotMode);
extern void __stdcall SendCmds		(int boardID, PVOID buffer, long cnt);
extern void __stdcall SendDataBytes	(int boardID, PVOID buffer, long cnt, int eot_mode);
extern void __stdcall SendIFC		(int boardID);
extern void __stdcall SendLLO		(int boardID);
extern void __stdcall SendList		(int boardID, Addr4882_t * addrlist, PVOID databuf, long datacnt, int eotMode);
extern void __stdcall SendSetup		(int boardID, Addr4882_t * addrlist);
extern void __stdcall SetRWLS		(int boardID, Addr4882_t * addrlist);
extern void __stdcall TestSRQ		(int boardID, PSHORT result);
extern void __stdcall TestSys		(int boardID, Addr4882_t * addrlist, PSHORT results);
extern void __stdcall Trigger		(int boardID, Addr4882_t addr);
extern void __stdcall TriggerList	(int boardID, Addr4882_t * addrlist);
extern void __stdcall WaitSRQ		(int boardID, PSHORT result);

#endif


#ifdef __cplusplus
}
#endif


#endif	// __GPCMDECL_H__

