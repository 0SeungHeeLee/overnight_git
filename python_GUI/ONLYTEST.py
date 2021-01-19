from class_GUI import *

if __name__ == "__main__":
	#객체 생성
	app = QApplication(sys.argv)		
	ex = GUI_APP()
	sys.exit(app.exec_())


#https://wikidocs.net/22074 참고는 여기서

#꾸미기
'''
color_tmp = QLabel('Red')
color_tmp.setStyleSheet("color: red;"
                    	"border-style: solid;"
                        "border-width: 2px;"
                        "border-color: #FA8072;"
                        "border-radius: 3px"
                        "background-color: #7FFFD4")
vbox = QVBoxLayout()
vbox.addWidget(lbl_red)
...
self.setLayout(vbox)
'''