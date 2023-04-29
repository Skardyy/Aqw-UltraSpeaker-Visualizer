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
            model: 5
            delegate: Row {               
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 10
                Text { text: "Item " + (index + 1 ) 
                color: "white"}
                Text { text: "Value " + (index + 1) 
                color: "white"}
            }
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
            Material.background: "#666fb7"
            onClicked: {
                myApp.on_button_clicked()
            }
        }
    }
}
