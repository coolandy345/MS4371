// GpibTestDlg.cpp : �C���v�������e�[�V���� �t�@�C��
//

#include "stdafx.h"
#include "GpibTest.h"
#include "GpibTestDlg.h"
#include "GpCmDecl.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#undef THIS_FILE
static char THIS_FILE[] = __FILE__;
#endif

/////////////////////////////////////////////////////////////////////////////
// �A�v���P�[�V�����̃o�[�W�������Ŏg���Ă��� CAboutDlg �_�C�A���O
DWORD	Dev;

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// �_�C�A���O �f�[�^
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard �͉��z�֐��̃I�[�o�[���C�h�𐶐����܂�
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV �̃T�|�[�g
	//}}AFX_VIRTUAL

// �C���v�������e�[�V����
protected:
	//{{AFX_MSG(CAboutDlg)
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
	//{{AFX_DATA_INIT(CAboutDlg)
	//}}AFX_DATA_INIT
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CAboutDlg)
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
	//{{AFX_MSG_MAP(CAboutDlg)
		// ���b�Z�[�W �n���h��������܂���B
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CGpibTestDlg �_�C�A���O

CGpibTestDlg::CGpibTestDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CGpibTestDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CGpibTestDlg)
		// ����: ���̈ʒu�� ClassWizard �ɂ���ă����o�̏��������ǉ�����܂��B
	//}}AFX_DATA_INIT
	// ����: LoadIcon �� Win32 �� DestroyIcon �̃T�u�V�[�P���X��v�����܂���B
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CGpibTestDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	//{{AFX_DATA_MAP(CGpibTestDlg)
	DDX_Control(pDX, IDC_EDIT4, m_SPoll);
	DDX_Control(pDX, IDC_EDIT3, m_Slave);
	DDX_Control(pDX, IDC_EDIT2, m_Master);
	DDX_Control(pDX, IDC_EDIT1, m_Address);
	//}}AFX_DATA_MAP
}

BEGIN_MESSAGE_MAP(CGpibTestDlg, CDialog)
	//{{AFX_MSG_MAP(CGpibTestDlg)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_Init, OnInit)
	ON_BN_CLICKED(IDC_Master, OnMaster)
	ON_BN_CLICKED(IDC_Slave, OnSlave)
	ON_BN_CLICKED(IDC_SPoll, OnSPoll)
	ON_BN_CLICKED(IDC_Exit, OnExit)
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CGpibTestDlg ���b�Z�[�W �n���h��

BOOL CGpibTestDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// "�o�[�W�������..." ���j���[���ڂ��V�X�e�� ���j���[�֒ǉ����܂��B

	// IDM_ABOUTBOX �̓R�}���h ���j���[�͈̔͂łȂ���΂Ȃ�܂���B
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// ���̃_�C�A���O�p�̃A�C�R����ݒ肵�܂��B�t���[�����[�N�̓A�v���P�[�V�����̃��C��
	// �E�B���h�E���_�C�A���O�łȂ����͎����I�ɐݒ肵�܂���B
	SetIcon(m_hIcon, TRUE);			// �傫���A�C�R����ݒ�
	SetIcon(m_hIcon, FALSE);		// �������A�C�R����ݒ�
	
	// TODO: ���ʂȏ��������s�����͂��̏ꏊ�ɒǉ����Ă��������B
	m_Address.SetWindowText("1");
	m_Master.SetWindowText("*IDN?");
	m_Slave.SetWindowText("");
	m_SPoll.SetWindowText("0");

	return TRUE;  // TRUE ��Ԃ��ƃR���g���[���ɐݒ肵���t�H�[�J�X�͎����܂���B
}

void CGpibTestDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// �����_�C�A���O�{�b�N�X�ɍŏ����{�^����ǉ�����Ȃ�΁A�A�C�R����`�悷��
// �R�[�h���ȉ��ɋL�q����K�v������܂��BMFC �A�v���P�[�V������ document/view
// ���f�����g���Ă���̂ŁA���̏����̓t���[�����[�N�ɂ�莩���I�ɏ�������܂��B

void CGpibTestDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // �`��p�̃f�o�C�X �R���e�L�X�g

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// �N���C�A���g�̋�`�̈���̒���
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// �A�C�R����`�悵�܂��B
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// �V�X�e���́A���[�U�[���ŏ����E�B���h�E���h���b�O���Ă���ԁA
// �J�[�\����\�����邽�߂ɂ������Ăяo���܂��B
HCURSOR CGpibTestDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CGpibTestDlg::OnInit() 
{
	// TODO: ���̈ʒu�ɃR���g���[���ʒm�n���h���p�̃R�[�h��ǉ����Ă�������
	char  address[100];
	DWORD pad;

	m_Address.GetWindowText(address,sizeof(address));
	pad = atoi(address);

   	Dev = ibdev (0, pad, 0, T10s, 1, 0);

	if ((ibsta & ERR) != 0) {
         MessageBox("Unable to open device");
    }
}

void CGpibTestDlg::OnMaster() 
{
	// TODO: ���̈ʒu�ɃR���g���[���ʒm�n���h���p�̃R�[�h��ǉ����Ă�������
	char wrtbuf[100];
	int nCnt;

	m_Master.GetWindowText(wrtbuf,sizeof(wrtbuf));

	nCnt = lstrlen(wrtbuf);
    ibwrt (Dev, wrtbuf, nCnt);

	if ((ibsta & ERR) != 0) {
        MessageBox("Unable to write to device");
    }
}

void CGpibTestDlg::OnSlave() 
{
	// TODO: ���̈ʒu�ɃR���g���[���ʒm�n���h���p�̃R�[�h��ǉ����Ă�������
	char rdbuf[100] = "";
		
	ibrd (Dev, rdbuf, sizeof(rdbuf));

	if ((ibsta & ERR) != 0) {
        MessageBox("Unable to read from device");
    }
	
	m_Slave.SetWindowText(rdbuf);
}

void CGpibTestDlg::OnSPoll() 
{
	// TODO: ���̈ʒu�ɃR���g���[���ʒm�n���h���p�̃R�[�h��ǉ����Ă�������
	char spr;
	char szBuff[10];

	ibrsp(Dev, &spr);
	
	if ((ibsta & ERR) != 0) {
        MessageBox("Unable to serial poll");
    }

	wsprintf(szBuff, "%x H", (int)spr);
	m_SPoll.SetWindowText(szBuff);
}

void CGpibTestDlg::OnExit() 
{
	// TODO: ���̈ʒu�ɃR���g���[���ʒm�n���h���p�̃R�[�h��ǉ����Ă�������
	ibonl(Dev, 0);
	CDialog::OnCancel();
}
