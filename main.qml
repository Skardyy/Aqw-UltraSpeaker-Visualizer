import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import MyApp 1.0

ApplicationWindow {
    visible: true
    width: 600
    height: 500
    title: "MyApp"
    color: "#0e1117"
    Material.accent: "#e91e63"

    MyApp {
        id: myApp
        onZone_change: zone_taker => titleText.text = zone_taker
        onBlock_change: blocks => {tauntModel.remove(0, tauntModel.count); tauntModel.append(blocks)}
    }

    Column {
        anchors.fill: parent
        spacing: 20

        Text {
            id: titleText
            anchors.horizontalCenter: parent.horizontalCenter
            text: "Title"
            color: "white"
            font.pixelSize: 24
        }

        ListView {
            id: itemList        
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            height: 200
            model: tauntModel
            interactive: false
            spacing: 8
            delegate: 
            Rectangle{   
                width: 200
                height: 35
                border.width: 1.5
                color: "#191b22"
                border.color: "red"           
                anchors.horizontalCenter: parent.horizontalCenter
                Row {
                    anchors.fill: parent
                    anchors.margins: 8  

                    Text {
                        text: word
                        color: "white"
                        anchors.left: parent.left
                        anchors.leftMargin: 10
                    }

                    Text{
                        id: emptyAlligner
                        anchors.right: parent.right
                        anchors.rightMargin: 25
                    }

                    Text { 
                        text: taunter
                        color: "white"
                        anchors.left: emptyAlligner.right
                    }
                }
            }      
        }
        ListModel{
            id: tauntModel
        }

        ComboBox {         
            anchors.horizontalCenter: parent.horizontalCenter
            id: playerDropdown
            Material.theme: Material.Dark
            popup.Material.foreground: "black"
            model: ["LR", "AP", "SC", "LOO"]
        }

        Row {    
            anchors.horizontalCenter: parent.horizontalCenter       
            Material.theme: Material.Dark
            spacing: 10
            CheckBox { id: lr_cb; text: "LR"}
            CheckBox { id: ap_cb; text: "AP"}
            CheckBox { id: sc_cb; text: "SC" }
            CheckBox { id: loo_cb; text: "LOO"}
        }

        Button {
            anchors.horizontalCenter: parent.horizontalCenter
            text: "<font color='white'>Apply</font>"
            Material.background: "#6c59d2"
            onClicked: {
                myApp.on_button_clicked()
            }
        }
    }
}
