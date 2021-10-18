Option Strict Off
Option Explicit On
Friend Class Form1
	Inherits System.Windows.Forms.Form
#Region "Windows フォーム デザイナによって生成されたコード"
	Public Sub New()
		MyBase.New()
		If m_vb6FormDefInstance Is Nothing Then
			If m_InitializingDefInstance Then
				m_vb6FormDefInstance = Me
			Else
				Try 
					'スタートアップ フォームについては、最初に作成されたインスタンスが既定インスタンスになります。
					If System.Reflection.Assembly.GetExecutingAssembly.EntryPoint.DeclaringType Is Me.GetType Then
						m_vb6FormDefInstance = Me
					End If
				Catch
				End Try
			End If
		End If
		'この呼び出しは、Windows フォーム デザイナで必要です。
		InitializeComponent()
	End Sub
	'Form は、コンポーネント一覧に後処理を実行するために dispose をオーバーライドします。
	Protected Overloads Overrides Sub Dispose(ByVal Disposing As Boolean)
		If Disposing Then
			If Not components Is Nothing Then
				components.Dispose()
			End If
		End If
		MyBase.Dispose(Disposing)
	End Sub
	'Windows フォーム デザイナで必要です。
	Private components As System.ComponentModel.IContainer
	Public ToolTip1 As System.Windows.Forms.ToolTip
	Public WithEvents Command1 As System.Windows.Forms.Button
	Public WithEvents SPoll As System.Windows.Forms.Button
	Public WithEvents Slave As System.Windows.Forms.Button
	Public WithEvents Master As System.Windows.Forms.Button
	Public WithEvents Init As System.Windows.Forms.Button
	Public WithEvents Poll As System.Windows.Forms.TextBox
	Public WithEvents Outp As System.Windows.Forms.TextBox
	Public WithEvents Inp As System.Windows.Forms.TextBox
	Public WithEvents Addr As System.Windows.Forms.TextBox
	Public WithEvents Label4 As System.Windows.Forms.Label
	Public WithEvents Label3 As System.Windows.Forms.Label
	Public WithEvents Label2 As System.Windows.Forms.Label
	Public WithEvents Label1 As System.Windows.Forms.Label
	'メモ : 以下のプロシージャは Windows フォーム デザイナで必要です。
	'Windows フォーム デザイナを使って変更できます。
	'コードエディタを使って修正しないでください。

	<System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Me.ToolTip1 = New System.Windows.Forms.ToolTip(Me.components)
        Me.Command1 = New System.Windows.Forms.Button()
        Me.SPoll = New System.Windows.Forms.Button()
        Me.Slave = New System.Windows.Forms.Button()
        Me.Master = New System.Windows.Forms.Button()
        Me.Init = New System.Windows.Forms.Button()
        Me.Poll = New System.Windows.Forms.TextBox()
        Me.Outp = New System.Windows.Forms.TextBox()
        Me.Inp = New System.Windows.Forms.TextBox()
        Me.Addr = New System.Windows.Forms.TextBox()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'Command1
        '
        Me.Command1.BackColor = System.Drawing.SystemColors.Control
        Me.Command1.Cursor = System.Windows.Forms.Cursors.Default
        Me.Command1.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Command1.Location = New System.Drawing.Point(320, 144)
        Me.Command1.Name = "Command1"
        Me.Command1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Command1.Size = New System.Drawing.Size(57, 25)
        Me.Command1.TabIndex = 12
        Me.Command1.Text = "終了"
        '
        'SPoll
        '
        Me.SPoll.BackColor = System.Drawing.SystemColors.Control
        Me.SPoll.Cursor = System.Windows.Forms.Cursors.Default
        Me.SPoll.ForeColor = System.Drawing.SystemColors.ControlText
        Me.SPoll.Location = New System.Drawing.Point(320, 112)
        Me.SPoll.Name = "SPoll"
        Me.SPoll.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.SPoll.Size = New System.Drawing.Size(57, 25)
        Me.SPoll.TabIndex = 7
        Me.SPoll.Text = "SPoll"
        '
        'Slave
        '
        Me.Slave.BackColor = System.Drawing.SystemColors.Control
        Me.Slave.Cursor = System.Windows.Forms.Cursors.Default
        Me.Slave.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Slave.Location = New System.Drawing.Point(320, 80)
        Me.Slave.Name = "Slave"
        Me.Slave.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Slave.Size = New System.Drawing.Size(57, 25)
        Me.Slave.TabIndex = 6
        Me.Slave.Text = "受信"
        '
        'Master
        '
        Me.Master.BackColor = System.Drawing.SystemColors.Control
        Me.Master.Cursor = System.Windows.Forms.Cursors.Default
        Me.Master.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Master.Location = New System.Drawing.Point(320, 48)
        Me.Master.Name = "Master"
        Me.Master.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Master.Size = New System.Drawing.Size(57, 25)
        Me.Master.TabIndex = 5
        Me.Master.Text = "送信"
        '
        'Init
        '
        Me.Init.BackColor = System.Drawing.SystemColors.Control
        Me.Init.Cursor = System.Windows.Forms.Cursors.Default
        Me.Init.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Init.Location = New System.Drawing.Point(320, 16)
        Me.Init.Name = "Init"
        Me.Init.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Init.Size = New System.Drawing.Size(57, 25)
        Me.Init.TabIndex = 4
        Me.Init.Text = "初期化"
        '
        'Poll
        '
        Me.Poll.AcceptsReturn = True
        Me.Poll.AutoSize = False
        Me.Poll.BackColor = System.Drawing.SystemColors.Window
        Me.Poll.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.Poll.ForeColor = System.Drawing.SystemColors.WindowText
        Me.Poll.Location = New System.Drawing.Point(72, 112)
        Me.Poll.MaxLength = 0
        Me.Poll.Name = "Poll"
        Me.Poll.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Poll.Size = New System.Drawing.Size(233, 18)
        Me.Poll.TabIndex = 3
        Me.Poll.Text = "Text4"
        '
        'Outp
        '
        Me.Outp.AcceptsReturn = True
        Me.Outp.AutoSize = False
        Me.Outp.BackColor = System.Drawing.SystemColors.Window
        Me.Outp.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.Outp.ForeColor = System.Drawing.SystemColors.WindowText
        Me.Outp.Location = New System.Drawing.Point(72, 80)
        Me.Outp.MaxLength = 0
        Me.Outp.Name = "Outp"
        Me.Outp.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Outp.Size = New System.Drawing.Size(233, 18)
        Me.Outp.TabIndex = 2
        Me.Outp.Text = "Text3"
        '
        'Inp
        '
        Me.Inp.AcceptsReturn = True
        Me.Inp.AutoSize = False
        Me.Inp.BackColor = System.Drawing.SystemColors.Window
        Me.Inp.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.Inp.ForeColor = System.Drawing.SystemColors.WindowText
        Me.Inp.Location = New System.Drawing.Point(72, 48)
        Me.Inp.MaxLength = 0
        Me.Inp.Name = "Inp"
        Me.Inp.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Inp.Size = New System.Drawing.Size(233, 18)
        Me.Inp.TabIndex = 1
        Me.Inp.Text = "Text2"
        '
        'Addr
        '
        Me.Addr.AcceptsReturn = True
        Me.Addr.AutoSize = False
        Me.Addr.BackColor = System.Drawing.SystemColors.Window
        Me.Addr.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.Addr.ForeColor = System.Drawing.SystemColors.WindowText
        Me.Addr.Location = New System.Drawing.Point(72, 16)
        Me.Addr.MaxLength = 0
        Me.Addr.Name = "Addr"
        Me.Addr.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Addr.Size = New System.Drawing.Size(89, 18)
        Me.Addr.TabIndex = 0
        Me.Addr.Text = "Text1"
        '
        'Label4
        '
        Me.Label4.BackColor = System.Drawing.Color.Transparent
        Me.Label4.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label4.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label4.Location = New System.Drawing.Point(8, 112)
        Me.Label4.Name = "Label4"
        Me.Label4.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label4.Size = New System.Drawing.Size(49, 17)
        Me.Label4.TabIndex = 11
        Me.Label4.Text = "SPoll"
        '
        'Label3
        '
        Me.Label3.BackColor = System.Drawing.Color.Transparent
        Me.Label3.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label3.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label3.Location = New System.Drawing.Point(8, 80)
        Me.Label3.Name = "Label3"
        Me.Label3.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label3.Size = New System.Drawing.Size(64, 17)
        Me.Label3.TabIndex = 10
        Me.Label3.Text = "受信データ"
        '
        'Label2
        '
        Me.Label2.BackColor = System.Drawing.Color.Transparent
        Me.Label2.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label2.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label2.Location = New System.Drawing.Point(8, 48)
        Me.Label2.Name = "Label2"
        Me.Label2.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label2.Size = New System.Drawing.Size(64, 17)
        Me.Label2.TabIndex = 9
        Me.Label2.Text = "送信データ"
        '
        'Label1
        '
        Me.Label1.BackColor = System.Drawing.Color.Transparent
        Me.Label1.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label1.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label1.Location = New System.Drawing.Point(8, 16)
        Me.Label1.Name = "Label1"
        Me.Label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label1.Size = New System.Drawing.Size(48, 17)
        Me.Label1.TabIndex = 8
        Me.Label1.Text = "アドレス"
        '
        'Form1
        '
        Me.ClientSize = New System.Drawing.Size(395, 179)
        Me.Controls.AddRange(New System.Windows.Forms.Control() {Me.Command1, Me.SPoll, Me.Slave, Me.Master, Me.Init, Me.Poll, Me.Outp, Me.Inp, Me.Addr, Me.Label4, Me.Label3, Me.Label2, Me.Label1})
        Me.Location = New System.Drawing.Point(4, 23)
        Me.Name = "Form1"
        Me.Text = "GpibTest"
        Me.ResumeLayout(False)

    End Sub
#End Region 
#Region "アップグレード ウィザードのサポート コード"
	Private Shared m_vb6FormDefInstance As Form1
	Private Shared m_InitializingDefInstance As Boolean
	Public Shared Property DefInstance() As Form1
		Get
			If m_vb6FormDefInstance Is Nothing OrElse m_vb6FormDefInstance.IsDisposed Then
				m_InitializingDefInstance = True
				m_vb6FormDefInstance = New Form1()
				m_InitializingDefInstance = False
			End If
			DefInstance = m_vb6FormDefInstance
		End Get
		Set
			m_vb6FormDefInstance = Value
		End Set
	End Property
#End Region 
	
    Const BDINDEX As Short = 0                              ' デバイス用アクセスボードの指標
    Const NO_SECONDARY_ADDR As Short = 0                    ' デバイスの2次GPIBアドレス
    Const TIMEOUT As Short = T10s                           ' 入出力タイムアウト値
    Const EOTMODE As Short = 1                              ' デバイスのEOIモード
    Const EOSMODE As Short = 0                              ' EOS文字とモード
	
    Const ARRAYSIZE As Short = 100                          ' Size of read buffer
	
	Dim ResByte As Short
	Dim Dev As Short
    Dim Valuestr As New String("", ARRAYSIZE)

    Dim ErrMsg As New String("", 100)
    Dim ErrorMnemonic As Object
	
	Private Sub Command1_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles Command1.Click
		
		Call ibonl(Dev, 0)
		End
		
	End Sub
	
	Private Sub Form1_Load(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles MyBase.Load
		
		Addr.Text = CStr(1)
		Inp.Text = "*IDN?"
		Outp.Text = ""
		Poll.Text = CStr(0)
		
	End Sub
	
	Private Sub Master_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles Master.Click
		
		Call ibwrt(Dev, Inp.Text)
		
		If (ibsta And EERR) Then
			Call GPIBCleanup("Unable to write to device")
		End If
		
	End Sub
	
	Private Sub Init_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles Init.Click
		Dim pad As Short
		
		pad = CShort(Addr.Text)
		Call ibdev(BDINDEX, pad, NO_SECONDARY_ADDR, TIMEOUT, EOTMODE, EOSMODE, Dev)
		
		If (ibsta And EERR) Then
            ErrMsg = "Unable to open device" & vbCrLf & "ibsta = &H" & Hex(ibsta) & vbCrLf & "iberr = " & iberr
            MsgBox(ErrMsg, MsgBoxStyle.Critical, "Error")
			End
		End If
		
	End Sub
	
	Private Sub Slave_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles Slave.Click
        Call ibrd(Dev, Valuestr)

        If (ibsta And EERR) Then
            Call GPIBCleanup("Unable to read from device")
        End If

        Outp.Text = Mid(Valuestr, 1, ibcntl(0))

    End Sub

    Private Sub SPoll_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles SPoll.Click

        Call ibrsp(Dev, ResByte)

        If (ibsta And EERR) Then
            Call GPIBCleanup("Unable to serial poll")
        End If

        Poll.Text = ResByte.ToString

    End Sub

    Private Sub GPIBCleanup(ByRef msg As String)
        Dim ErrMsg As String

        ' After each GPIB call, the application checks whether the call
        ' succeeded. If an NI-488.2 call fails, the GPIB driver sets the
        ' corresponding bit in the global status variable. If the call
        ' failed, this procedure prints an error message, takes the device
        ' offline and exits.

        ErrorMnemonic = New Object() {"EDVR", "ECIC", "ENOL", "EADR", "EARG", "ESAC", "EABO", "ENEB", "EDMA", "", "EOIP", "ECAP", "EFSO", "", "EBUS", "ESTB", "ESRQ", "", "", "", "ETAB"}


        ErrMsg = msg & vbCrLf & "ibsta = &H" & Hex(ibsta) & vbCrLf & "iberr = " & iberr & " <" & ErrorMnemonic(iberr) & ">"
        MsgBox(ErrMsg, MsgBoxStyle.Critical, "Error")

    End Sub
End Class