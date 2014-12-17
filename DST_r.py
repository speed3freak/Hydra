
class node:
	def __init__(self, range_bits,node_length,headsh,key_length):
		self.range_bits = range_bits << node_length # pad range_bits
		self.node_length = node_length
		self.head_shift = headsh
		self.key_length = key_length
		self.num_shifts = (self.key_length-self.node_length)/self.head_shift
		self.values = {}
		#table containing masked bit ranges associated with other nodes
		self.f_table = {}
		
	def get_value(self, key):
		rbm = 0 #to store range bitmasked
		kbm = 0#to store key bitmasked
		bitmask = (2^self.head_shift - 1) #fill with correct number of ones
		bitmask = bitmask << (self.node_length + (self.num_shifts-1)*self.head_shift) #skip over node stored bits
		#todo skip over alread processed bits
		for i in range(0,self.num_shifts):
			rbm = self.range_bits&bitmask
			kbm = key&bitmask
			print("offset %i" %i)
			print("bitmask: %s" %bin(bitmask))
			print("rbm: %s" %bin(rbm))
			print("kbm: %s" %bin(kbm))
			if rbm == kbm:
				bitmask = bitmask >> (self.head_shift)
			else:
				print("value not found contact other node")
				return False
		#if it gets here key is in node's range check table
		if key in self.values:
		  return self.values[key]
		else:
		  return False

	def add_value(self,key,value):
	  #todo check if it is in range
		self.values[key]=value
		
		
node = node(int('001011',2),2,2,8)
node.add_value(int('00101110',2),True)
print node.get_value(int('00101110',2))