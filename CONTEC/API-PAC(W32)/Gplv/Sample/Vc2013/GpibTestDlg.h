// GpibTestDlg.h : ヘッダー ファイル
//

#if !defined(AFX_GPIBTESTDLG_H__305FA6BD_F69C_41DE_8808_CE66C219BECA__INCLUDED_)
#define AFX_GPIBTESTDLG_H__305FA6BD_F69C_41DE_8808_CE66C219BECA__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CGpibTestDlg ダイアログ

class CGpibTestDlg : public CDialog
{
// 構築
public:
	CGpibTestDlg(CWnd* pParent = NULL);	// 標準のコンストラクタ

// ダイアログ データ
	//{{AFX_DATA(CGpibTestDlg)
	enum { IDD = IDD_GPIBTEST_DIALOG };
	CEdit	m_SPoll;
	CEdit	m_Slave;
	CEdit	m_Master;
	CEdit	m_Address;
	//}}AFX_DATA

	// ClassWizard は仮想関数のオーバーライドを生成します。
	//{{AFX_VIRTUAL(CGpibTestDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV のサポート
	//}}AFX_VIRTUAL

// インプリメンテーション
protected:
	HICON m_hIcon;

	// 生成されたメッセージ マップ関数
	//{{AFX_MSG(CGpibTestDlg)
	virtual BOOL OnInitDialog();
	afx_msg void OnSysCommand(UINT nID, LPARAM lParam);
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	afx_msg void OnInit();
	afx_msg void OnMaster();
	afx_msg void OnSlave();
	afx_msg void OnSPoll();
	afx_msg void OnExit();
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ は前行の直前に追加の宣言を挿入します。

#endif // !defined(AFX_GPIBTESTDLG_H__305FA6BD_F69C_41DE_8808_CE66C219BECA__INCLUDED_)
