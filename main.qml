import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.15
import MyApp 1.0

ApplicationWindow {
    visible: true
    width: 250
    height: 350
    title: "Aqw UltraSpeaker dynamic chart"
    color: "#0e1117"
    Material.accent: "#e91e63"

    MyApp {
        id: myApp
        onZone_change: zone_taker => {
            titleText.text = zone_taker;
            titleText.color = (zone_taker == playerDropdown.currentText) ? 'red' : 'white'
        }
        onBlock_change: lst => {tauntModel.clear() ; tauntModel.append(lst)}
    }

    Column {
        anchors.fill: parent
        spacing: 5

        Text {
            id: titleText
            anchors.horizontalCenter: parent.horizontalCenter
            text: "None"
            color: "white"
            font.pixelSize: 24
        }

        ListView {
            id: itemList        
            anchors.horizontalCenter: parent.horizontalCenter
            width: parent.width
            height: 175
            model: tauntModel
            interactive: false
            spacing: 8
            delegate: 
            Rectangle{   
                width: 200
                height: 35
                border.width: 1.5
                color: "#191b22"
                border.color: me ? "red" : "transparent"
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
            width: 200
            height: 40
            anchors.horizontalCenter: parent.horizontalCenter
            id: playerDropdown
            Material.theme: Material.Dark
            popup.Material.foreground: "black"
            model: ["LR", "AP", "SC", "LOO"]
        }

        Row {    
            width: 225
            height: 40
            anchors.horizontalCenter: parent.horizontalCenter       
            Material.theme: Material.Dark
            CheckBox { id: lr_cb; text: "LR"}
            CheckBox { id: ap_cb; text: "AP"}
            CheckBox { id: sc_cb; text: "SC" }
            CheckBox { id: loo_cb; text: "LOO"}
        }

        Button {
            width: 200
            height: 40
            anchors.horizontalCenter: parent.horizontalCenter
            text: "<font color='white'>Apply</font>"
            Material.background: "#6c59d2"
            onClicked: {
                myApp.apply(lr_cb.checked, loo_cb.checked, ap_cb.checked, sc_cb.checked)
            }
        }
    }
}
