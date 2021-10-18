// GpibTestDlg.cpp : インプリメンテーション ファイル
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
// アプリケーションのバージョン情報で使われている CAboutDlg ダイアログ
DWORD	Dev;

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// ダイアログ データ
	//{{AFX_DATA(CAboutDlg)
	enum { IDD = IDD_ABOUTBOX };
	//}}AFX_DATA

	// ClassWizard は仮想関数のオーバーライドを生成します
	//{{AFX_VIRTUAL(CAboutDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV のサポート
	//}}AFX_VIRTUAL

// インプリメンテーション
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
		// メッセージ ハンドラがありません。
	//}}AFX_MSG_MAP
END_MESSAGE_MAP()

/////////////////////////////////////////////////////////////////////////////
// CGpibTestDlg ダイアログ

CGpibTestDlg::CGpibTestDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CGpibTestDlg::IDD, pParent)
{
	//{{AFX_DATA_INIT(CGpibTestDlg)
		// メモ: この位置に ClassWizard によってメンバの初期化が追加されます。
	//}}AFX_DATA_INIT
	// メモ: LoadIcon は Win32 の DestroyIcon のサブシーケンスを要求しません。
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
// CGpibTestDlg メッセージ ハンドラ

BOOL CGpibTestDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// "バージョン情報..." メニュー項目をシステム メニューへ追加します。

	// IDM_ABOUTBOX はコマンド メニューの範囲でなければなりません。
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

	// このダイアログ用のアイコンを設定します。フレームワークはアプリケーションのメイン
	// ウィンドウがダイアログでない時は自動的に設定しません。
	SetIcon(m_hIcon, TRUE);			// 大きいアイコンを設定
	SetIcon(m_hIcon, FALSE);		// 小さいアイコンを設定
	
	// TODO: 特別な初期化を行う時はこの場所に追加してください。
	m_Address.SetWindowText("1");
	m_Master.SetWindowText("*IDN?");
	m_Slave.SetWindowText("");
	m_SPoll.SetWindowText("0");

	return TRUE;  // TRUE を返すとコントロールに設定したフォーカスは失われません。
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

// もしダイアログボックスに最小化ボタンを追加するならば、アイコンを描画する
// コードを以下に記述する必要があります。MFC アプリケーションは document/view
// モデルを使っているので、この処理はフレームワークにより自動的に処理されます。

void CGpibTestDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 描画用のデバイス コンテキスト

		SendMessage(WM_ICONERASEBKGND, (WPARAM) dc.GetSafeHdc(), 0);

		// クライアントの矩形領域内の中央
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// アイコンを描画します。
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// システムは、ユーザーが最小化ウィンドウをドラッグしている間、
// カーソルを表示するためにここを呼び出します。
HCURSOR CGpibTestDlg::OnQueryDragIcon()
{
	return (HCURSOR) m_hIcon;
}

void CGpibTestDlg::OnInit() 
{
	// TODO: この位置にコントロール通知ハンドラ用のコードを追加してください
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
	// TODO: この位置にコントロール通知ハンドラ用のコードを追加してください
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
	// TODO: この位置にコントロール通知ハンドラ用のコードを追加してください
	char rdbuf[100] = "";
		
	ibrd (Dev, rdbuf, sizeof(rdbuf));

	if ((ibsta & ERR) != 0) {
        MessageBox("Unable to read from device");
    }
	
	m_Slave.SetWindowText(rdbuf);
}

void CGpibTestDlg::OnSPoll() 
{
	// TODO: この位置にコントロール通知ハンドラ用のコードを追加してください
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
	// TODO: この位置にコントロール通知ハンドラ用のコードを追加してください
	ibonl(Dev, 0);
	CDialog::OnCancel();
}
