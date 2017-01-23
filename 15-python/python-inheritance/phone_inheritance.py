class Phone:
  def __init__(self, phone_number):
    self.number = phone_number
    
  def call(self, other_number):
    print("Calling {} from {}.".format(other_number, self.number))
    
  def text(self, other_number, msg):
    print("Sending text from {} to {}:".format(self.number, other_number))
    print(msg);
    
class IPhone(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.fingerprint = None
    
  def set_fingerprint(self, fingerprint):
    self.fingerprint = fingerprint
    
  def unlock(self, fingerprint=None):
    if (self.fingerprint == None):
      print("Phone unlocked because no fingerprint has not been set.")
      
    if (fingerprint == self.fingerprint):
      print("Phone unlocked. Fingerprint matches.")
    else:
      print("Phone locked. Fingerprint doesn't match.")
  
class Android(Phone):
  def __init__(self, phone_number):
    super().__init__(phone_number)
    self.keyboard = "Default"
    
  def set_keyboard(self, keyboard):
    self.keyboard = keyboard
    
moms_number = "888-3434"
old_phone = Phone("555-1314")
iphone = IPhone("555-0001")
android = Android("555-1337")

# All phones have the call method defined in Phone
old_phone.call(moms_number)
iphone.call(moms_number)
android.call(moms_number)
print()

# All phones have the text method defined in Phone
old_phone.text(moms_number, "Hey Mom. I want a new phone.")
iphone.text(moms_number, "Thanks for the iPhone, Mom!")
android.text(moms_number, "Mom, I saved up and bought an Android.")
print()

# made up strings representing "fingerprints"
my_fingerprint = "swirl whorl whorl"
other_fingerprint = "spiral whorl swirl"

# the iphone has access to it's own unlock and set_fingerprint methods.
iphone.unlock()

iphone.set_fingerprint(my_fingerprint)
iphone.unlock(other_fingerprint)
iphone.unlock(my_fingerprint)
print()

# the Android starts with the default keyboard and users can change
# it to use a custom Swype keyboard
print("The Android phone is using the {} keyboard".format(android.keyboard))
android.set_keyboard("Swype")
print("The Android phone is using the {} keyboard".format(android.keyboard))

# This code will break because sub-classes only have extra functionality
# defined in their own class. iPhones don't get Android stuff and vice versa.
# The iPhone doesn't have access to the set_keyboard method.
# The Android doesn't have access to the set_fingerprint or unlock methods.
#
# This code will crash the program if uncommented:
# iphone.set_keyboard("iphones can't change keyboards")
# android.set_fingerprint("androids don't have fingerprint unlock")
