// GpibTestDlg.h : �w�b�_�[ �t�@�C��
//

#if !defined(AFX_GPIBTESTDLG_H__305FA6BD_F69C_41DE_8808_CE66C219BECA__INCLUDED_)
#define AFX_GPIBTESTDLG_H__305FA6BD_F69C_41DE_8808_CE66C219BECA__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

/////////////////////////////////////////////////////////////////////////////
// CGpibTestDlg �_�C�A���O

class CGpibTestDlg : public CDialog
{
// �\�z
public:
	CGpibTestDlg(CWnd* pParent = NULL);	// �W���̃R���X�g���N�^

// �_�C�A���O �f�[�^
	//{{AFX_DATA(CGpibTestDlg)
	enum { IDD = IDD_GPIBTEST_DIALOG };
	CEdit	m_SPoll;
	CEdit	m_Slave;
	CEdit	m_Master;
	CEdit	m_Address;
	//}}AFX_DATA

	// ClassWizard �͉��z�֐��̃I�[�o�[���C�h�𐶐����܂��B
	//{{AFX_VIRTUAL(CGpibTestDlg)
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV �̃T�|�[�g
	//}}AFX_VIRTUAL

// �C���v�������e�[�V����
protected:
	HICON m_hIcon;

	// �������ꂽ���b�Z�[�W �}�b�v�֐�
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
// Microsoft Visual C++ �͑O�s�̒��O�ɒǉ��̐錾��}�����܂��B

#endif // !defined(AFX_GPIBTESTDLG_H__305FA6BD_F69C_41DE_8808_CE66C219BECA__INCLUDED_)
