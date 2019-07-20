
# What is the difference between IBOutlet and IBAction in Swift?
An IBOutlet (Interface Builder outlet) is a variable which is a reference to a UI component. An IBAction (Interface Builder action) is a function which is called when a specific user interaction occurs. You want work to happen when you hit a button? You create an IBAction and define the work inside of it.

IBActions trigger code to run, and IBOutlets let code affect the UI.

IBAction reaches from UI elements to code, for example, allowing us to have a function execute when a button is pressed.

IBOutlet reaches from code to UI elements, for example, allowing us to set the text of a label.

When working with outlets and actions, you can check that they are hooked up by looking for filled-in circles in the gutter to the left of the code.



[Getting the User's Attention with Alerts and Action Sheets](https://developer.apple.com/documentation/uikit/windows_and_screens/getting_the_user_s_attention_with_alerts_and_action_sheets#2936078)



Add user interface elements in iOS

* build the first part of the Pitch Perfect app by adding and connecting buttons from an interface to code.
* How to add a UIbutton and setting up the text and background color.
* A system for positioning UI elements on screen called auto layout
  * layout constraints are the rules you give auto layout so that it can do its work
  * intrinsic size, that is they have a built in height and width.
  * then it only needs one additional constraint on each axis. iOS can automatically calculate the spacing on the remaining sides. You need a minimum of two constraints on each axis to properly lay out a UI element.
  * 至少知道要知道兩個方向的長度



2種加上 constraint 的方式

1. 用右下角的 align
2. 按下 control 拖拉物件到你要的 view 後藉由 dialog 去點選 constraint

I’m going to hold down the control key and click drag to the View. 

What is the difference between an IBOutlet and an IBAction?

IBActions trigger code to run, and IBOutlets let code affect the UI.

![](../.gitbook/assets/ios_2.png)

