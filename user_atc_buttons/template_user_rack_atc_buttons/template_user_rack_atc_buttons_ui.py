# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'template_user_rack_atc_buttons.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

from qtpyvcp.widgets.button_widgets.mdi_button import MDIButton
from qtpyvcp.widgets.button_widgets.subcall_button import SubCallButton

class Ui_USER_ATC_BUTTONS(object):
    def setupUi(self, USER_ATC_BUTTONS):
        if not USER_ATC_BUTTONS.objectName():
            USER_ATC_BUTTONS.setObjectName(u"USER_ATC_BUTTONS")
        USER_ATC_BUTTONS.resize(300, 429)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(USER_ATC_BUTTONS.sizePolicy().hasHeightForWidth())
        USER_ATC_BUTTONS.setSizePolicy(sizePolicy)
        USER_ATC_BUTTONS.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout = QVBoxLayout(USER_ATC_BUTTONS)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.user_atc_buttons_frame = QFrame(USER_ATC_BUTTONS)
        self.user_atc_buttons_frame.setObjectName(u"user_atc_buttons_frame")
        sizePolicy.setHeightForWidth(self.user_atc_buttons_frame.sizePolicy().hasHeightForWidth())
        self.user_atc_buttons_frame.setSizePolicy(sizePolicy)
        self.user_atc_buttons_frame.setMaximumSize(QSize(300, 16777215))
        self.user_atc_buttons_frame.setStyleSheet(u"")
        self.verticalLayout_66 = QVBoxLayout(self.user_atc_buttons_frame)
        self.verticalLayout_66.setSpacing(16)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(20, 18, 20, 18)
        self.atc_rack_user_header = QLabel(self.user_atc_buttons_frame)
        self.atc_rack_user_header.setObjectName(u"atc_rack_user_header")
        self.atc_rack_user_header.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.atc_rack_user_header.sizePolicy().hasHeightForWidth())
        self.atc_rack_user_header.setSizePolicy(sizePolicy1)
        self.atc_rack_user_header.setMinimumSize(QSize(0, 38))
        self.atc_rack_user_header.setMaximumSize(QSize(16777215, 38))
        self.atc_rack_user_header.setStyleSheet(u"QLabel{\n"
"    border-style: solid;\n"
"    border-color: rgb(176, 179, 172);\n"
"    border-width: 2px;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    background: rgb(90, 90, 90);\n"
"	font: 16pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.atc_rack_user_header.setFrameShape(QFrame.Shape.NoFrame)
        self.atc_rack_user_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.atc_rack_user_header.setWordWrap(True)
        self.atc_rack_user_header.setIndent(0)

        self.verticalLayout_66.addWidget(self.atc_rack_user_header)

        self.user_buttons_row1_layout = QHBoxLayout()
        self.user_buttons_row1_layout.setSpacing(15)
        self.user_buttons_row1_layout.setObjectName(u"user_buttons_row1_layout")
        self.user_buttons_row1_layout.setContentsMargins(2, 2, 2, 2)
        self.air_blast_button = MDIButton(self.user_atc_buttons_frame)
        self.air_blast_button.setObjectName(u"air_blast_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.air_blast_button.sizePolicy().hasHeightForWidth())
        self.air_blast_button.setSizePolicy(sizePolicy2)
        self.air_blast_button.setMinimumSize(QSize(120, 45))
        self.air_blast_button.setMaximumSize(QSize(16777215, 45))
        self.air_blast_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.air_blast_button.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.air_blast_button.setIconSize(QSize(20, 20))

        self.user_buttons_row1_layout.addWidget(self.air_blast_button)

        self.retract_dustboot_button = MDIButton(self.user_atc_buttons_frame)
        self.retract_dustboot_button.setObjectName(u"retract_dustboot_button")
        sizePolicy2.setHeightForWidth(self.retract_dustboot_button.sizePolicy().hasHeightForWidth())
        self.retract_dustboot_button.setSizePolicy(sizePolicy2)
        self.retract_dustboot_button.setMinimumSize(QSize(120, 45))
        self.retract_dustboot_button.setMaximumSize(QSize(16777215, 45))
        self.retract_dustboot_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.retract_dustboot_button.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.retract_dustboot_button.setIconSize(QSize(20, 20))

        self.user_buttons_row1_layout.addWidget(self.retract_dustboot_button)


        self.verticalLayout_66.addLayout(self.user_buttons_row1_layout)

        self.user_buttons_row2_layout = QHBoxLayout()
        self.user_buttons_row2_layout.setSpacing(15)
        self.user_buttons_row2_layout.setObjectName(u"user_buttons_row2_layout")
        self.user_buttons_row2_layout.setContentsMargins(2, 2, 2, 2)
        self.clamp_tool_button = SubCallButton(self.user_atc_buttons_frame)
        self.clamp_tool_button.setObjectName(u"clamp_tool_button")
        sizePolicy2.setHeightForWidth(self.clamp_tool_button.sizePolicy().hasHeightForWidth())
        self.clamp_tool_button.setSizePolicy(sizePolicy2)
        self.clamp_tool_button.setMinimumSize(QSize(120, 45))
        self.clamp_tool_button.setMaximumSize(QSize(16777215, 45))
        self.clamp_tool_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.user_buttons_row2_layout.addWidget(self.clamp_tool_button)

        self.release_tool_button = SubCallButton(self.user_atc_buttons_frame)
        self.release_tool_button.setObjectName(u"release_tool_button")
        self.release_tool_button.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.release_tool_button.sizePolicy().hasHeightForWidth())
        self.release_tool_button.setSizePolicy(sizePolicy2)
        self.release_tool_button.setMinimumSize(QSize(120, 45))
        self.release_tool_button.setMaximumSize(QSize(16777215, 45))
        self.release_tool_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.user_buttons_row2_layout.addWidget(self.release_tool_button)


        self.verticalLayout_66.addLayout(self.user_buttons_row2_layout)

        self.user_buttons_row3_layout = QHBoxLayout()
        self.user_buttons_row3_layout.setSpacing(15)
        self.user_buttons_row3_layout.setObjectName(u"user_buttons_row3_layout")
        self.user_buttons_row3_layout.setContentsMargins(2, 2, 2, 2)
        self.spindle_orientation_button = SubCallButton(self.user_atc_buttons_frame)
        self.spindle_orientation_button.setObjectName(u"spindle_orientation_button")
        sizePolicy2.setHeightForWidth(self.spindle_orientation_button.sizePolicy().hasHeightForWidth())
        self.spindle_orientation_button.setSizePolicy(sizePolicy2)
        self.spindle_orientation_button.setMinimumSize(QSize(120, 45))
        self.spindle_orientation_button.setMaximumSize(QSize(16777215, 45))
        self.spindle_orientation_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")
        self.spindle_orientation_button.setCheckable(True)

        self.user_buttons_row3_layout.addWidget(self.spindle_orientation_button)

        self.unlock_spindle_button = MDIButton(self.user_atc_buttons_frame)
        self.unlock_spindle_button.setObjectName(u"unlock_spindle_button")
        sizePolicy2.setHeightForWidth(self.unlock_spindle_button.sizePolicy().hasHeightForWidth())
        self.unlock_spindle_button.setSizePolicy(sizePolicy2)
        self.unlock_spindle_button.setMinimumSize(QSize(120, 45))
        self.unlock_spindle_button.setMaximumSize(QSize(16777215, 45))
        self.unlock_spindle_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.unlock_spindle_button.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.unlock_spindle_button.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.unlock_spindle_button.setIconSize(QSize(20, 20))

        self.user_buttons_row3_layout.addWidget(self.unlock_spindle_button)


        self.verticalLayout_66.addLayout(self.user_buttons_row3_layout)

        self.user_buttons_row4_layout = QHBoxLayout()
        self.user_buttons_row4_layout.setSpacing(15)
        self.user_buttons_row4_layout.setObjectName(u"user_buttons_row4_layout")
        self.user_buttons_row4_layout.setContentsMargins(2, 2, 2, 2)
        self.move_head_up_button = SubCallButton(self.user_atc_buttons_frame)
        self.move_head_up_button.setObjectName(u"move_head_up_button")
        sizePolicy2.setHeightForWidth(self.move_head_up_button.sizePolicy().hasHeightForWidth())
        self.move_head_up_button.setSizePolicy(sizePolicy2)
        self.move_head_up_button.setMinimumSize(QSize(120, 45))
        self.move_head_up_button.setMaximumSize(QSize(16777215, 45))
        self.move_head_up_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.user_buttons_row4_layout.addWidget(self.move_head_up_button)

        self.move_head_down_button = SubCallButton(self.user_atc_buttons_frame)
        self.move_head_down_button.setObjectName(u"move_head_down_button")
        sizePolicy2.setHeightForWidth(self.move_head_down_button.sizePolicy().hasHeightForWidth())
        self.move_head_down_button.setSizePolicy(sizePolicy2)
        self.move_head_down_button.setMinimumSize(QSize(120, 45))
        self.move_head_down_button.setMaximumSize(QSize(16777215, 45))
        self.move_head_down_button.setStyleSheet(u"SubCallButton {\n"
"    color: white;\n"
"    border-color: black;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    border-width: 2px;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));\n"
"    font-family: \"Probe Basic Bebas Mono\";\n"
"    font-size: 15pt;\n"
"}\n"
"\n"
"SubCallButton:disabled {\n"
"    border-color: gray;\n"
"}\n"
"\n"
"SubCallButton:hover {\n"
"    background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #A19E9E, stop: 1.0 #5C5959);\n"
"}\n"
"\n"
"SubCallButton:pressed {\n"
"    background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));\n"
"}\n"
"")

        self.user_buttons_row4_layout.addWidget(self.move_head_down_button)


        self.verticalLayout_66.addLayout(self.user_buttons_row4_layout)

        self.widget_10 = QWidget(self.user_atc_buttons_frame)
        self.widget_10.setObjectName(u"widget_10")

        self.verticalLayout_66.addWidget(self.widget_10)

        self.user_buttons_row5_layout = QHBoxLayout()
        self.user_buttons_row5_layout.setSpacing(15)
        self.user_buttons_row5_layout.setObjectName(u"user_buttons_row5_layout")
        self.user_buttons_row5_layout.setContentsMargins(2, 2, 2, 2)
        self.Ref_rack_button = MDIButton(self.user_atc_buttons_frame)
        self.Ref_rack_button.setObjectName(u"Ref_rack_button")
        sizePolicy2.setHeightForWidth(self.Ref_rack_button.sizePolicy().hasHeightForWidth())
        self.Ref_rack_button.setSizePolicy(sizePolicy2)
        self.Ref_rack_button.setMinimumSize(QSize(125, 45))
        self.Ref_rack_button.setMaximumSize(QSize(16777215, 45))
        self.Ref_rack_button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.Ref_rack_button.setStyleSheet(u"MDIButton {\n"
"    font: 15pt \"Probe Basic Bebas Mono\";\n"
"}")
        self.Ref_rack_button.setIconSize(QSize(20, 20))

        self.user_buttons_row5_layout.addWidget(self.Ref_rack_button)


        self.verticalLayout_66.addLayout(self.user_buttons_row5_layout)


        self.verticalLayout.addWidget(self.user_atc_buttons_frame)


        self.retranslateUi(USER_ATC_BUTTONS)

        QMetaObject.connectSlotsByName(USER_ATC_BUTTONS)
    # setupUi

    def retranslateUi(self, USER_ATC_BUTTONS):
        USER_ATC_BUTTONS.setWindowTitle(QCoreApplication.translate("USER_ATC_BUTTONS", u"User Atc Buttons", None))
        self.atc_rack_user_header.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"ATC MANUAL CONTROL PANEL", None))
#if QT_CONFIG(tooltip)
        self.air_blast_button.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.air_blast_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"AIR BLAST", None))
        self.air_blast_button.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
#if QT_CONFIG(tooltip)
        self.retract_dustboot_button.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.retract_dustboot_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"RETR DUST BOOT", None))
        self.retract_dustboot_button.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
        self.clamp_tool_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"CLAMP TOOL", None))
        self.clamp_tool_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"clamptool.ngc", None))
        self.release_tool_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"RELEASE TOOL", None))
        self.release_tool_button.setProperty(u"rules", QCoreApplication.translate("USER_ATC_BUTTONS", u"[{\"name\": \"spindle safety\", \"property\": \"Enable\", \"expression\": \"not ch[0]\", \"channels\": [{\"url\": \"status:spindle.0.enabled\", \"trigger\": true}]}]", None))
        self.release_tool_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"unclamptool.ngc", None))
        self.spindle_orientation_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"ORIENT SPINDLE", None))
        self.spindle_orientation_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"orientspindle.ngc", None))
#if QT_CONFIG(tooltip)
        self.unlock_spindle_button.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M112 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.unlock_spindle_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"UNLOCK SPINDLE", None))
        self.unlock_spindle_button.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M5", None))
        self.move_head_up_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"HEAD UP", None))
        self.move_head_up_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"move_head_above_carousel.ngc", None))
        self.move_head_down_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"HEAD DOWN", None))
        self.move_head_down_button.setProperty(u"filename", QCoreApplication.translate("USER_ATC_BUTTONS", u"move_tool_to_carousel_height.ngc", None))
#if QT_CONFIG(tooltip)
        self.Ref_rack_button.setToolTip(QCoreApplication.translate("USER_ATC_BUTTONS", u"M13 User Defined Macro Call from Subroutine Folder", None))
#endif // QT_CONFIG(tooltip)
        self.Ref_rack_button.setText(QCoreApplication.translate("USER_ATC_BUTTONS", u"REF RACK DATA", None))
        self.Ref_rack_button.setProperty(u"MDICommand", QCoreApplication.translate("USER_ATC_BUTTONS", u"M13", None))
    # retranslateUi

