# Capstone Project
## Blender Custom Nodes
In this Project we have to make Custom Blender Nodes with the help bpy library.
Nodes are similar to a function, but it has a User Interface. A node can have input sockets and output sockets. 
We can connect one output socket with another nodes' input socket to manipulate the data flow.

In this project we are going to make Nodes which will take some inputs manually and with the help of Faker Library we 
have to output a customized random data(It can be string/color/number/etc.).

### Random Barcode Generator
```
class MyRandomBarcode(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeBarcode'
    bl_label = 'Random Barcode'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new('CustomSocketType', 'EAN Type')
        self.inputs.new("NodeSocketString", "Comma Separated Prefixes")

        self.outputs.new('NodeSocketString', 'RBarcode')

    def update(self):
        inpt1 = self.inputs[0].my_enum_prop
        inpt2 = self.inputs[1].default_value
        print(inpt1)
        print(f"Prefixes: {inpt2}")
        oupt = self.outputs[0].default_value
        oupt = fake.ean(length=int(inpt1), prefixes=inpt2.split(","))
        print(oupt)

    def draw_label(self):
        return "Barcode"
```
It has two Input sockets, One lets you select the EAN type and second lets you have custom prefixes for barcode.
The First input has a Custom Socket Type of dropdown menu. The second input has a String Socket type. The Output will be a String type which contains the Barcode.
### Random Credit Card Generator
```
lass MyRandomCreditCard(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeCreditCard'
    bl_label = 'Random Credit Card'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new('NodeSocketBool', 'Card Provider')
        self.inputs.new('NodeSocketBool', 'Name')
        self.inputs.new('NodeSocketBool', 'Card Number')
        self.inputs.new('NodeSocketBool', 'Card Expiry Date')
        self.inputs.new('NodeSocketBool', 'Card Security Code')

        self.outputs.new('NodeSocketString', 'RCreditCard')

    def update(self):
        option1 = self.inputs[0].default_value
        option2 = self.inputs[1].default_value
        option3 = self.inputs[2].default_value
        option4 = self.inputs[3].default_value
        option5 = self.inputs[4].default_value
        oupt = self.outputs[0].default_value
        if option1:
            oupt += fake.credit_card_provider()
            oupt += '\n'
        if option2:
            oupt += fake.name()
            oupt += '\n'
        if option3:
            oupt += fake.credit_card_number()
            oupt += '\n'
        if option4:
            oupt += fake.credit_card_expire()
            oupt += '\n'
        if option5:
            oupt += fake.credit_card_security_code()
            oupt += '\n'
        print(oupt)

    def draw_label(self):
        return "Credit Card"
```
This Node has many Input Sockets which can be used to Customize to output. 
For Example, if I want only the Name and Card Number, I can tick those options and the output will be generated 
with only Name and Number strings.
### Random SSN Generator
```
class MyRandomSSN(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeSSN'
    bl_label = 'Random SSN'
    bl_icon = 'ACTION'

    def init(self, context):
        self.outputs.new('NodeSocketString', 'RSSN')

    def update(self):
        oupt = self.outputs[0].default_value
        oupt = fake.ssn()
        print(oupt)

    def draw_label(self):
        return "SSN"
```
This Node has no input and will output a random SSN Number everytime the links are refreshed.
### Random Address Generator
```
class MyRandomAddress(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeAddress'
    bl_label = 'Random Address'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new("NodeSocketBool", "Street Address")
        self.inputs.new("NodeSocketBool", "City")
        self.inputs.new("NodeSocketBool", "Country")
        self.inputs.new("NodeSocketBool", "Postcode")

        self.outputs.new('NodeSocketString', 'Address')

    def update(self):
        option1 = self.inputs[0].default_value
        option2 = self.inputs[1].default_value
        option3 = self.inputs[2].default_value
        option4 = self.inputs[3].default_value
        oupt = self.outputs[0].default_value
        if option1:
            oupt += fake.street_address()
            oupt += '\n'
        if option2:
            oupt += fake.city()
            oupt += '\n'
        if option3:
            oupt += fake.country()
            oupt += '\n'
        if option4:
            oupt += fake.postcode()
            oupt += '\n'
        print(oupt)

    def draw_label(self):
        return "Address"
```
Just like the Credit Card Node, we can customize the output by selecting the required values.
### Random License Generator
```
class MyRandomAutomotive(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeAutomotive'
    bl_label = 'Random Automotive'
    bl_icon = 'ACTION'

    def init(self, context):
        self.outputs.new('NodeSocketString', 'License')

    def update(self):
        oupt = self.outputs[0].default_value
        oupt = fake.license_plate()
        print(oupt)

    def draw_label(self):
        return "License"
```
This node generates Random Licenses. It does not have any inputs like the SSN Node.
### Random Color Generator
```
class MyRandomColor(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeColor'
    bl_label = 'Random Color'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new("CustomSocketType2", "Hue")
        self.inputs.new("CustomSocketType3", "Luminosity")
        self.inputs.new("CustomSocketType4", "Color Format")

        self.outputs.new('NodeSocketString', 'Color')

    def update(self):
        option1 = self.inputs[0].my_enum_prop
        option2 = self.inputs[1].my_enum_prop
        option3 = self.inputs[2].my_enum_prop
        oupt = self.outputs[0].default_value
        oupt = fake.color(hue=option1, luminosity=option2, color_format=option3)
        print(oupt)

    def draw_label(self):
        return "Color"
```
This Node is the most intresting useful of all nodes. We can choose what ype of Hue we want,
we can choose the type of luminosity and the output color format. 
All the inputs ae custom sockets which are a Dropdown Menu.
### Random Company Generator
```
class MyRandomCompany(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeCompany'
    bl_label = 'Random Company'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new("NodeSocketBool", "Name")
        self.inputs.new("NodeSocketBool", "Catch Phrase")
        self.inputs.new("NodeSocketBool", "Description")

        self.outputs.new('NodeSocketString', 'Company')

    def update(self):
        option1 = self.inputs[0].default_value
        option2 = self.inputs[1].default_value
        option3 = self.inputs[2].default_value
        oupt = self.outputs[0].default_value
        if option1:
            oupt += fake.company()
            oupt += '\n'
        if option2:
            oupt += fake.catch_phrase()
            oupt += '\n'
        if option3:
            oupt += fake.bs()
            oupt += '\n'
        print(oupt)

    def draw_label(self):
        return "Company"
```
This Node provides us with a Ranodm Company Name, a Catch Phrase and a Description. We can customize the output also.
### Random Job Generator
```
class MyRandomJob(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodeJob'
    bl_label = 'Random Job'
    bl_icon = 'ACTION'

    def init(self, context):
        self.outputs.new('NodeSocketString', 'Job')

    def update(self):
        oupt = self.outputs[0].default_value
        oupt = fake.job()
        print(oupt)

    def draw_label(self):
        return "Job"
```
This node does not take any input and provides us with a randomly generated Job Title.
### Random Phone Number Generator
```
class MyRandomPhoneNumber(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodePhoneNumber'
    bl_label = 'Random PhoneNumber'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new("NodeSocketBool", "MSISDN")
        self.inputs.new("NodeSocketBool", "Phone Number")

        self.outputs.new('NodeSocketString', 'Number')

    def update(self):
        option1 = self.inputs[0].default_value
        option2 = self.inputs[1].default_value
        oupt = self.outputs[0].default_value
        if option1:
            oupt += fake.msisdn()
            oupt += '\n'
        if option2:
            oupt += fake.phone_number()
            oupt += '\n'
        print(oupt)

    def draw_label(self):
        return "PhoneNumber"
```
This node has two options, MSISDN and Phone Number, and will output the following numbers if they are choosen.
### Random Person Name Generator
```
class MyRandomPerson(Node, MyCustomTreeNode):
    bl_idname = 'CustomNodePerson'
    bl_label = 'Random Person'
    bl_icon = 'ACTION'

    def init(self, context):
        self.inputs.new("CustomSocketType5", "Gender")
        self.inputs.new("NodeSocketBool", "Prefix")
        self.inputs.new("NodeSocketBool", "First Name")
        self.inputs.new("NodeSocketBool", "Last Name")

        self.outputs.new('NodeSocketString', 'Person')

    def update(self):
        option1 = self.inputs[0].my_enum_prop
        option2 = self.inputs[1].default_value
        option3 = self.inputs[2].default_value
        option4 = self.inputs[3].default_value
        oupt = self.outputs[0].default_value
        if option1 == 'male':
            if option2:
                oupt += fake.prefix_male()
                oupt += ' '
            if option3:
                oupt += fake.first_name_male()
                oupt += ' '
            if option4:
                oupt += fake.last_name_male()
                oupt += ' '
        else:
            if option2:
                oupt += fake.prefix_female()
                oupt += ' '
            if option3:
                oupt += fake.first_name_female()
                oupt += ' '
            if option4:
                oupt += fake.last_name_female()
                oupt += ' '
        print(oupt)

    def draw_label(self):
        return "Person"
```
This has 4 inputs, Gender, Prefix, First name and Last name. 
Gender input socket is Custom made ie Dropdown Menu and rest all are Check Boxes.
This will provide us with random Names as per our choices.

## How to use Nodes
1. Install Blender
2. Type `from pip._internal import main`, `main(['install','faker'])` in Python Console
3. This will install Faker Library to your Blenders' Python
4. Run the Python Script
5. Open System Terminal
6. Click on Add -> Fake Nodes -> Choose Node