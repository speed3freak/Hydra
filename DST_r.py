
node = node(int('001011',2),2,2,8)
node.add_value(int('00101110',2)


class node():
	def __init__(self, range_bits,node_length,headsh,key_length):
		self.range_bits = range_bits << node_length # pad range_bits
		self.node_length = node_length
		self.head_shift = headsh
		self.key_length = key_length
		self.num_shifts = (self.key_length-self.node_length)/self.head_shift
		self.values = {}
		
	def get_value(self, key):
		rbm = 0 #to store range bitmasked
		kbm = 0#to store key bitmasked
		bitmask = (2^headshift - 1) #fill with correct number of ones
		bitmask = bitmask << (val_length) #skip over node stored bits
		#todo skip over alread processed bits
		for shift in range(num_shifts,0,-1):
			bitmask= bitmask << (self.head_shift*shift)
			rbm = self.range_bits&bitmask
			kbm = key&bitmask
			if rbm == kbm:
				continue
			else:
				print("value not found contacting other node")

	def add_value(self,key,value):
		self.values[key]=value
