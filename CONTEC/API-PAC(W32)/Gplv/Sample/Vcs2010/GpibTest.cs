using System;
using System.Drawing;
using System.Collections;
using System.ComponentModel;
using System.Windows.Forms;
using System.Data;
using System.Text;
using CGpCmDeclCs;

namespace GpibTest
{
	/// <summary>
	/// Form1 の概要の説明です。
	/// </summary>
	public class GpibTest : System.Windows.Forms.Form
	{
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label label3;
		private System.Windows.Forms.Label label4;
		private System.Windows.Forms.Button btnInit;
		private System.Windows.Forms.Button btnMaster;
		private System.Windows.Forms.Button btnSlave;
		private System.Windows.Forms.Button btnSPoll;
		private System.Windows.Forms.Button btnExit;
		private System.Windows.Forms.TextBox txtAddress;
		private System.Windows.Forms.TextBox txtMaster;
		private System.Windows.Forms.TextBox txtSlave;
		private System.Windows.Forms.TextBox txtSPoll;
		/// <summary>
		/// 必要なデザイナ変数です。
		/// </summary>
		private System.ComponentModel.Container components = null;

		CGpCmDecl	GpCmDecl = new CGpCmDecl();

		int			Dev;
		int			Ret;

		public GpibTest()
		{
			//
			// Windows フォーム デザイナ サポートに必要です。
			//
			InitializeComponent();

			//
			// TODO: InitializeComponent 呼び出しの後に、コンストラクタ コードを追加してください。
			//
		}

		/// <summary>
		/// 使用されているリソースに後処理を実行します。
		/// </summary>
		protected override void Dispose( bool disposing )
		{
			if( disposing )
			{
				if (components != null) 
				{
					components.Dispose();
				}
			}
			base.Dispose( disposing );
		}

		#region Windows Form Designer generated code
		/// <summary>
		/// デザイナ サポートに必要なメソッドです。このメソッドの内容を
		/// コード エディタで変更しないでください。
		/// </summary>
		private void InitializeComponent()
		{
			this.btnInit = new System.Windows.Forms.Button();
			this.btnMaster = new System.Windows.Forms.Button();
			this.btnSlave = new System.Windows.Forms.Button();
			this.btnSPoll = new System.Windows.Forms.Button();
			this.btnExit = new System.Windows.Forms.Button();
			this.label1 = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.label3 = new System.Windows.Forms.Label();
			this.label4 = new System.Windows.Forms.Label();
			this.txtAddress = new System.Windows.Forms.TextBox();
			this.txtMaster = new System.Windows.Forms.TextBox();
			this.txtSlave = new System.Windows.Forms.TextBox();
			this.txtSPoll = new System.Windows.Forms.TextBox();
			this.SuspendLayout();
			// 
			// btnInit
			// 
			this.btnInit.Location = new System.Drawing.Point(312, 20);
			this.btnInit.Name = "btnInit";
			this.btnInit.Size = new System.Drawing.Size(80, 24);
			this.btnInit.TabIndex = 0;
			this.btnInit.Text = "初期化";
			this.btnInit.Click += new System.EventHandler(this.btnInit_Click);
			// 
			// btnMaster
			// 
			this.btnMaster.Location = new System.Drawing.Point(312, 52);
			this.btnMaster.Name = "btnMaster";
			this.btnMaster.Size = new System.Drawing.Size(80, 24);
			this.btnMaster.TabIndex = 1;
			this.btnMaster.Text = "送信";
			this.btnMaster.Click += new System.EventHandler(this.btnMaster_Click);
			// 
			// btnSlave
			// 
			this.btnSlave.Location = new System.Drawing.Point(312, 84);
			this.btnSlave.Name = "btnSlave";
			this.btnSlave.Size = new System.Drawing.Size(80, 24);
			this.btnSlave.TabIndex = 2;
			this.btnSlave.Text = "受信";
			this.btnSlave.Click += new System.EventHandler(this.btnSlave_Click);
			// 
			// btnSPoll
			// 
			this.btnSPoll.Location = new System.Drawing.Point(312, 116);
			this.btnSPoll.Name = "btnSPoll";
			this.btnSPoll.Size = new System.Drawing.Size(80, 24);
			this.btnSPoll.TabIndex = 3;
			this.btnSPoll.Text = "SPoll";
			this.btnSPoll.Click += new System.EventHandler(this.btnSPoll_Click);
			// 
			// btnExit
			// 
			this.btnExit.Location = new System.Drawing.Point(312, 148);
			this.btnExit.Name = "btnExit";
			this.btnExit.Size = new System.Drawing.Size(80, 24);
			this.btnExit.TabIndex = 4;
			this.btnExit.Text = "終了";
			this.btnExit.Click += new System.EventHandler(this.btnExit_Click);
			// 
			// label1
			// 
			this.label1.Location = new System.Drawing.Point(24, 24);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(64, 16);
			this.label1.TabIndex = 5;
			this.label1.Text = "アドレス";
			// 
			// label2
			// 
			this.label2.Location = new System.Drawing.Point(24, 56);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(64, 16);
			this.label2.TabIndex = 6;
			this.label2.Text = "送信データ";
			// 
			// label3
			// 
			this.label3.Location = new System.Drawing.Point(24, 88);
			this.label3.Name = "label3";
			this.label3.Size = new System.Drawing.Size(64, 16);
			this.label3.TabIndex = 7;
			this.label3.Text = "受信データ";
			// 
			// label4
			// 
			this.label4.Location = new System.Drawing.Point(24, 120);
			this.label4.Name = "label4";
			this.label4.Size = new System.Drawing.Size(64, 16);
			this.label4.TabIndex = 8;
			this.label4.Text = "SPoll";
			// 
			// txtAddress
			// 
			this.txtAddress.Location = new System.Drawing.Point(96, 23);
			this.txtAddress.Name = "txtAddress";
			this.txtAddress.Size = new System.Drawing.Size(56, 19);
			this.txtAddress.TabIndex = 9;
			this.txtAddress.Text = "";
			// 
			// txtMaster
			// 
			this.txtMaster.Location = new System.Drawing.Point(96, 55);
			this.txtMaster.Name = "txtMaster";
			this.txtMaster.Size = new System.Drawing.Size(200, 19);
			this.txtMaster.TabIndex = 10;
			this.txtMaster.Text = "";
			// 
			// txtSlave
			// 
			this.txtSlave.Location = new System.Drawing.Point(96, 87);
			this.txtSlave.Name = "txtSlave";
			this.txtSlave.Size = new System.Drawing.Size(200, 19);
			this.txtSlave.TabIndex = 11;
			this.txtSlave.Text = "";
			// 
			// txtSPoll
			// 
			this.txtSPoll.Location = new System.Drawing.Point(96, 119);
			this.txtSPoll.Name = "txtSPoll";
			this.txtSPoll.Size = new System.Drawing.Size(200, 19);
			this.txtSPoll.TabIndex = 12;
			this.txtSPoll.Text = "";
			// 
			// GpibTest
			// 
			this.ClientSize = new System.Drawing.Size(426, 184);
			this.Controls.AddRange(new System.Windows.Forms.Control[] {
																		  this.txtSPoll,
																		  this.txtSlave,
																		  this.txtMaster,
																		  this.txtAddress,
																		  this.label4,
																		  this.label3,
																		  this.label2,
																		  this.label1,
																		  this.btnExit,
																		  this.btnSPoll,
																		  this.btnSlave,
																		  this.btnMaster,
																		  this.btnInit});
			this.Font = new System.Drawing.Font("ＭＳ Ｐゴシック", 9F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((System.Byte)(128)));
			this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
			this.MaximizeBox = false;
			this.MinimizeBox = false;
			this.Name = "GpibTest";
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
			this.Text = "GpibTest";
			this.Load += new System.EventHandler(this.GpibTest_Load);
			this.Closed += new System.EventHandler(this.GpibTest_Closed);
			this.ResumeLayout(false);

		}
		#endregion

		/// <summary>
		/// アプリケーションのメイン エントリ ポイントです。
		/// </summary>
		[STAThread]
		static void Main() 
		{
			Application.Run(new GpibTest());
		}

		private void GpibTest_Load(object sender, System.EventArgs e)
		{
			txtAddress.Text = "1";
			txtMaster.Text = "*IDN?";
			txtSlave.Text = "";
			txtSPoll.Text = "0";
		}

		private void GpibTest_Closed(object sender, System.EventArgs e)
		{
			GpCmDecl.Pkibonl(Dev, 0);
		}

		private void btnInit_Click(object sender, System.EventArgs e)
		{
			string	address = new string(' ', 100);
			int		pad;

			address = txtAddress.Text;
			try
			{
				pad = Convert.ToInt32(address);
			}
			catch (System.FormatException)
			{
				pad = 0;
			}

			Dev = GpCmDecl.Pkibdev(0, pad, 0, (int)CGpCmDeclConst.T10s, 1, 0);

			Ret = GpCmDecl.PkThreadIbsta();
			if ((Ret & (int)CGpCmDeclConst.ERR) != 0)
			{
				MessageBox.Show("Unable to open device");
			}
		}

		private void btnMaster_Click(object sender, System.EventArgs e)
		{
			string	wrtbuf = new string(' ', 100);
			int		nCnt;

			wrtbuf = txtMaster.Text;

			nCnt = wrtbuf.Length;
			GpCmDecl.Pkibwrt(Dev, wrtbuf, nCnt);

			Ret = GpCmDecl.PkThreadIbsta();
			if ((Ret & (int)CGpCmDeclConst.ERR) != 0)
			{
				MessageBox.Show("Unable to write to device");
			}
		}

		private void btnSlave_Click(object sender, System.EventArgs e)
		{
			StringBuilder rdbuf = new StringBuilder("", 100);
		
			GpCmDecl.Pkibrd(Dev, rdbuf, rdbuf.Capacity);
			int	nCnt = GpCmDecl.PkThreadIbcntl();

			Ret = GpCmDecl.PkThreadIbsta();
			if ((Ret & (int)CGpCmDeclConst.ERR) != 0)
			{
				MessageBox.Show("Unable to read from device");
			}
	
			txtSlave.Text = rdbuf.ToString(0, nCnt);
		}

		private void btnSPoll_Click(object sender, System.EventArgs e)
		{
			char	spr;
			string	szBuff = new string(' ', 10);

			GpCmDecl.Pkibrsp(Dev, out spr);
	
			Ret = GpCmDecl.PkThreadIbsta();
			if ((Ret & (int)CGpCmDeclConst.ERR) != 0)
			{
				MessageBox.Show("Unable to serial poll");
			}

			txtSPoll.Text = string.Format("{0:x} H", (int)spr);
		}

		private void btnExit_Click(object sender, System.EventArgs e)
		{
			GpCmDecl.Pkibonl(Dev, 0);
			this.Close();
		}
	}
}
