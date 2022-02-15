# ------------------------> Imports <------------------------
import datetime
import bpy
from bpy.types import NodeTree, Node, NodeSocket
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
from faker import Faker

fake = Faker()


class MyCustomTree(NodeTree):
    bl_idname = 'CustomTreeType'
    bl_label = "Custom Node Tree"
    bl_icon = 'NODETREE'


class MyCustomTreeNode:
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'CustomTreeType'

# ------------------------> Custom Sockets <------------------------
# Every class should have a unique bl_idname which will be used by Blender Internally
class MyCustomSocket1(NodeSocket):
    '''
    This Custom Node Socket is used for Random Barcode Node.
    '''
    bl_idname = 'CustomSocketType'
    bl_label = "Custom Node Socket"
    my_items = (
        ('13', "EAN-13", "Length = 13"), # ("What will be stored", "What will be showed", "Description")
        ('8', "EAN-8", "Lenghth = 8"),
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="EAN Type",
        description="Choose Length of Barcode",
        items=my_items,
        default='13',
    )

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    def draw_color(self, context, node):
        return 1.0, 0.4, 0.216, 1


class MyCustomSocket2(NodeSocket):
    '''
    This Custom Node Socket is used for Random Color Node.
    '''
    bl_idname = 'CustomSocketType2'
    bl_label = "Custom Node Socket 2"
    my_items = (
        ('monochrome', "monochrome", " "),
        ('red', "red", " "),
        ('orange', "orange", " "),
        ('yellow', "yellow", " "),
        ('green', "green", " "),
        ('blue', "blue", " "),
        ('purple', "purple", " "),
        ('pink', "pink", " ")
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="Hue",
        description="Choose Hue Type",
        items=my_items,
        default='monochrome'
    )

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    def draw_color(self, context, node):
        return 0.3, 0.1, 0.7, 1


class MyCustomSocket3(NodeSocket):
    '''
    This Custom Node Socket is used for Random Color Node.
    '''
    bl_idname = 'CustomSocketType3'
    bl_label = "Custom Node Socket 3"
    my_items = (
        ('bright', "bright", ""),
        ('dark', "dark", ""),
        ('light', "light", ""),
        ('random', "random", "")
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="Luminosity",
        description="Choose Luminosity Type",
        items=my_items,
        default='light'
    )

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    def draw_color(self, context, node):
        return 0.1, 0.9, 0.5, 1


class MyCustomSocket4(NodeSocket):
    '''
    This Custom Node Socket is used for Random Color Node.
    '''
    bl_idname = 'CustomSocketType4'
    bl_label = "Custom Node Socket 4"
    my_items = (
        ('hsl', "hsl", ""),
        ('hsv', "hsv", ""),
        ('rgb', "rgb", ""),
        ('hex', "hex", "")
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="Color Format",
        description="Choose Color Format",
        items=my_items,
        default='rgb'
    )

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    def draw_color(self, context, node):
        return 0.9, 0.5, 0.9, 1


class MyCustomSocket5(NodeSocket):
    '''
    This Custom Node Socket is used for Random Person Node.
    '''
    bl_idname = 'CustomSocketType5'
    bl_label = "Custom Node Socket 5"
    my_items = (
        ('male', "Male", ""),
        ('female', "Female", ""),
    )

    my_enum_prop: bpy.props.EnumProperty(
        name="Gender",
        description="Choose Gender",
        items=my_items,
        default='male'
    )

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "my_enum_prop", text=text)

    def draw_color(self, context, node):
        return 0.4, 0.5, 0.5, 1

# ------------------------> Custom Nodes <------------------------
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


class MyRandomCreditCard(Node, MyCustomTreeNode):
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


class MyNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'CustomTreeType'


node_categories = [
    MyNodeCategory('OPNODES', "Faker Nodes", items=[
        NodeItem("CustomNodeBarcode"),
        NodeItem("CustomNodeCreditCard"),
        NodeItem("CustomNodeSSN"),
        NodeItem("CustomNodeAddress"),
        NodeItem("CustomNodeAutomotive"),
        NodeItem("CustomNodeColor"),
        NodeItem("CustomNodeCompany"),
        NodeItem("CustomNodeJob"),
        NodeItem("CustomNodePhoneNumber"),
        NodeItem("CustomNodePerson")
    ])
]

classes = (
    MyCustomTree,
    MyCustomSocket1,
    MyCustomSocket2,
    MyCustomSocket3,
    MyCustomSocket4,
    MyCustomSocket5,
    MyRandomBarcode,
    MyRandomCreditCard,
    MyRandomSSN,
    MyRandomAddress,
    MyRandomAutomotive,
    MyRandomColor,
    MyRandomCompany,
    MyRandomJob,
    MyRandomPhoneNumber,
    MyRandomPerson
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    nodeitems_utils.register_node_categories('CUSTOM_NODES', node_categories)


def unregister():
    nodeitems_utils.unregister_node_categories('CUSTOM_NODES')

    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
#    unregister()
