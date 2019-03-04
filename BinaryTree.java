package com.java.multithreading;

class TreeNode {
	int data;
	TreeNode left;
	TreeNode right;

	private String name;

	public TreeNode(int data, TreeNode left, TreeNode right, String name) {
		this.data = data;
		this.left = left;
		this.right = right;
		this.name = name;
	}

	public String getName() {
		return name;
	}

}

public class BinaryTree {

	TreeNode root = null;

	final int LEFT = -1;
	final int RIGHT = 1;

	public TreeNode createNode(int data, String nodeName) {
		TreeNode newNode = new TreeNode(data, null, null, nodeName);
		if (root == null) {
			root = newNode;
		}
		return newNode;
	}

	/**
	 * Inorder traversal: left, root, right need to traverse all the sub-trees in
	 * the same order.
	 */

	public void inorder(TreeNode node) {
		if (node.left != null)
			inorder(node.left);
		System.out.println("Visited node: " + node.getName() + ", it's value: " + node.data);
		if (node.right != null)
			inorder(node.right);
	}

	/**
	 * Preorder traversal: root, left, right need to traverse all the sub-trees in
	 * the same order
	 * 
	 */

	public void preorder(TreeNode node) {
		if (node != null) {
			System.out.println("Visited node: " + node.getName() + ", it's value: " + node.data);
			if (node.left != null)
				preorder(node.left);
			if (node.right != null)
				preorder(node.right);
		}
	}

	/**
	 * Postorder traversal: left, right, root need to traverse all the sub-trees in
	 * the same order
	 *  
	 */
	
	public void postorder(TreeNode node) {
		if(node.left != null)
			postorder(node.left);
		if(node.right != null)
			postorder(node.right);
		if(node != null)
			System.out.println("Visited node: " + node.getName() + ", it's value: " + node.data);
	}
	
	
	public void addNode(int data, TreeNode node, int pos, String nodeName) {
		if (pos == LEFT) {
			node.left = createNode(data, nodeName);
		} else if (pos == RIGHT) {
			node.right = createNode(data, nodeName);
		} else {
			System.out.println("Improper position");
		}
	}


	public void displayTreeData(BinaryTree binaryTree) {
		// createNode();
		System.out.println("In order traversal:");
		inorder(binaryTree.root);
		System.out.println("Pre order traversal:");
		preorder(binaryTree.root);
		System.out.println("Post order traversal:");
		postorder(binaryTree.root);
	}

	public static void main(String ar[]) {
		BinaryTree binaryTree = new BinaryTree();
		binaryTree = binaryTree.prepareBinaryTree();
		binaryTree.displayTreeData(binaryTree);
	}

	private BinaryTree prepareBinaryTree() {
		BinaryTree binaryTree = new BinaryTree();
		binaryTree.createNode(10, "Root");
		binaryTree.addNode(20, binaryTree.root, binaryTree.LEFT, "A");
		binaryTree.addNode(30, binaryTree.root, binaryTree.RIGHT, "B");
		binaryTree.addNode(40, binaryTree.root.left, binaryTree.LEFT, "C");
		binaryTree.addNode(50, binaryTree.root.left, binaryTree.RIGHT, "D");
		binaryTree.addNode(60, binaryTree.root.right, binaryTree.LEFT, "E");
		binaryTree.addNode(70, binaryTree.root.right, binaryTree.RIGHT, "F");
		binaryTree.addNode(80, binaryTree.root.left.right, binaryTree.LEFT, "G");
		return binaryTree;
	}

}
