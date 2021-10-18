// GpibTest.h : GPIBTEST アプリケーションのメイン ヘッダー ファイルです。
//

#if !defined(AFX_GPIBTEST_H__5C692952_20F1_4BCF_A9D9_5C7BC6D4E092__INCLUDED_)
#define AFX_GPIBTEST_H__5C692952_20F1_4BCF_A9D9_5C7BC6D4E092__INCLUDED_

#if _MSC_VER > 1000
#pragma once
#endif // _MSC_VER > 1000

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// メイン シンボル

/////////////////////////////////////////////////////////////////////////////
// CGpibTestApp:
// このクラスの動作の定義に関しては GpibTest.cpp ファイルを参照してください。
//

class CGpibTestApp : public CWinApp
{
public:
	CGpibTestApp();

// オーバーライド
	// ClassWizard は仮想関数のオーバーライドを生成します。
	//{{AFX_VIRTUAL(CGpibTestApp)
	public:
	virtual BOOL InitInstance();
	//}}AFX_VIRTUAL

// インプリメンテーション

	//{{AFX_MSG(CGpibTestApp)
		// メモ - ClassWizard はこの位置にメンバ関数を追加または削除します。
		//        この位置に生成されるコードを編集しないでください。
	//}}AFX_MSG
	DECLARE_MESSAGE_MAP()
};


/////////////////////////////////////////////////////////////////////////////

//{{AFX_INSERT_LOCATION}}
// Microsoft Visual C++ は前行の直前に追加の宣言を挿入します。

#endif // !defined(AFX_GPIBTEST_H__5C692952_20F1_4BCF_A9D9_5C7BC6D4E092__INCLUDED_)
