import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class GUI_APP(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.set_menuBar()
		self.set_toolBar()
		self.set_quitButton()
		self.set_interface()
		self.set_interfaceLocation()
		self.show()

	def set_interface(self):
		'''
		QDate. : 날짜 이용 / QTime. : 시간 이용 / QDateTime : 둘다 이용
		.currentDateTime() : 현재 시간 따기
		.toString() : str화 시키기 / Qt.DefaultLocaleLongDate 와 Qt.DefaultLocaleShortDate 알아서 잘 스까쓰기
		.setWindowTitle("name") : 타이틀 바 제목 정하기
		.move(x,y) : 창을 위치(x,y)로 이동 (단위 px)
		.resize(x,y) : 창 크기를 (x,y)만큼 조정 (단위 px)
		.show() : 위젯을 스크린에 표시
		.setWindowIcon(QIcon('file')) : 보여줄 아이콘 설정 (아마 아이콘은 따로 import된듯?)
		.setGeometry(x,y,width,height) : .move() + .resize()
		.statusBar().showMessage('Text') : 상태바 추가 및 해당 텍스트 출력
		'''

		str_dateTime = QDateTime.currentDateTime().toString('yyyy.MM.dd, hh:mm:ss')
		# QD = QDate.currentDate()
		# QT = QTime.currentTime()
		# str_date = QD.currentDate().toString('yyyy.MM.dd')
		# str_time = QT.toString('QT.DefaultLocaleLongDate')
		self.statusBar().showMessage(str_dateTime)
		self.setWindowTitle("Bithumb Trade Bot (TEST)")
		# self.setGeometry(300, 300, 1000, 1000)
		# self.move(300,300)
		self.resize(1600,1000)				#16:10 비율 기반
		self.setWindowIcon(QIcon('web.png'))



	def set_interfaceLocation(self):
		'''
		.frameGeometry() : 창 위치, 크기 정보 가져오기
		.QDesktopWidget().availableGeometry().center() : 현재 사용하는 모니터의 중앙위치 파악
		.moveCenter(cp) : 창 중앙으로
		.move(qr.topLeft()) 현재 창을 화면의 중심으로 이동했던 직사각형의 위치로 이동
		'''
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def set_quitButton(self):
		'''
		QPushButton('Text', widget)": 해당 부모위젯에서 Text 내용의 푸시버튼 생성
		.sizeHint(): 아마도 크기 지정??
		.clicked.connect(): 버튼 클릭시 clicked 시그널 생성 후 함수 내 메서드 연결 (변수 -> app)
		QCoreApplication.instance().quit : 대충 종료 명령
		QToolTip.setFont(QFont('font', size)) : 툴팁 텍스트꼴,크기 설정
		.setToolTip('Text') :버튼에 툴팁 추가
		'''
		quit_button = QPushButton('Quit', self)
		quit_button.move(50, 50)
		quit_button.resize(quit_button.sizeHint())
		QToolTip.setFont(QFont('SansSerif', 10))
		quit_button.setToolTip('ㅇㅋ <b>ㅇㅋ</b> ㅇㅋ')
		quit_button.clicked.connect(QCoreApplication.instance().quit)
	def set_menuBar(self):
		'''
		QAction(QIcon('img'), 'text', self) : img, text에 대한 동작 생성
		.setShortcut('ShortCut') : 단축키 지정 (메뉴 활성화 아니여도 작동)+
		.setStatusTip('Text') : 메뉴에 커서를 가져다 댈 경우 상태창에 보여줄 텍스트
		.triggered.connect(method) : 해당 동작 선택시 발생시킬 메서드
		.addMenu('&Locate') : 메뉴 분류
		.addAction(변수) : 액션 지정
		'''
		action_exit = QAction(QIcon('exit.png'), 'Exit', self)
		action_exit.setShortcut('Ctrl+Q')
		action_exit.setStatusTip('Exit application')
		action_exit.triggered.connect(qApp.quit)
		bar_menu = self.menuBar()
		bar_menu.setNativeMenuBar(False)
		menu_file = bar_menu.addMenu('&File')
		menu_file.addAction(action_exit)
	def set_toolBar(self):
		'''
		달라진것: self.addToolBar('Exit') <-> self.menuBar() 사용의 차이
		'''
		toolbar_exit = QAction(QIcon('exit.png'), 'Exit', self)
		toolbar_exit.setShortcut('Ctrl+Q')
		toolbar_exit.setStatusTip('Exit application')
		toolbar_exit.triggered.connect(qApp.quit)

		self.statusBar()
		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(toolbar_exit)