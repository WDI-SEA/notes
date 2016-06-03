class TreeNode
	attr_accessor :data, :left, :right

	# left and right nodes default to nil if not provided
	def initialize(data, left=nil, right=nil)
		@data = data
		@left = left
		@right = right
	end
end

class Tree
	attr_accessor :root

	def initialize()
		@root = nil
	end

	def to_s()
		return print_node(root)
	end

	private

	def print_node(node)
		# initialize the string as an empty string
		s = ""

		if node != nil
			# append the data at the current node
			s += " " + node.data.to_s

			# recursively append strings returned from printing
			# the left and right nodes.
			s += print_node(node.left)
			s += print_node(node.right)
		end

		# return the string
		return s
	end
end

# build a tree 
#    3 <-- root
#   / \
# 12   8

# create individual nodes for the tree
node1 = TreeNode.new(3)
node2 = TreeNode.new(12)
node3 = TreeNode.new(8)

# create a tree
tree = Tree.new

# attach node1 to the root
tree.root = node1

# attach nodes 2 and 3 to the left and right sides of the root
tree.root.left = node2
tree.root.right = node3

# print it!
puts tree