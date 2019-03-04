package com.java.multithreading;

public class BinarySearchTree extends BinaryTree {

	static TreeNode root;

	public TreeNode insertIntoBST(int data, TreeNode node, String name) {
		if (root == null) {
			root = createNode(data, "");
		} else {
			TreeNode next = root;
			TreeNode prev = root;
			while (next != null) {
				prev = next;
				if (next.data > data) {
					next = next.left;
				} else {
					next = next.right;
				}
			}
			if (prev != null) {
				if (prev.data > data) {
					prev.left = createNode(data, name);
				} else {
					prev.right = createNode(data, name);
				}
			}
		}

		return node;
	}

	public static void main(String ar[]) {
		BinarySearchTree bst = new BinarySearchTree();
		TreeNode trav = null;
		root = bst.createNode(30, "Root");
		trav = bst.insertIntoBST(20, root,"A");
		trav = bst.insertIntoBST(10, trav,"B");
		// 8,3,1,6,7,10,14,4
		//7 , 5 , 1 , 8 , 3 , 6 , 0 , 9 , 4 , 2
		//30 , 20 , 10 , 15 , 25 , 23 , 39 , 35 , 42
		trav = bst.insertIntoBST(15, trav,"C");
		trav = bst.insertIntoBST(25, trav,"D");
		trav = bst.insertIntoBST(23, trav,"E");
		trav = bst.insertIntoBST(39, trav,"F");
		trav = bst.insertIntoBST(35, trav,"G");
		trav = bst.insertIntoBST(42, trav,"H");
		//trav = bst.insertIntoBST(2, trav);
		// bst.insertIntoBST(4, root);
		System.out.println("*****************IN ORDER**************");
		bst.inorder(root);
		System.out.println("*****************POST ORDER************");
		bst.postorder(root);
		
		System.out.println("******Search an element********");
		boolean flag = bst.searchAlgo(100, root);
		System.out.println("Element found: "+flag);
		
	}

	public boolean searchAlgo(int data, TreeNode root) {
		boolean flag = false;
		try {
			if(root != null) {
				if(root.data == data) {
					flag = true;					
				} else if(data < root.data) {
					return searchAlgo(data, root.left);
				} else if(data > root.data){
					return searchAlgo(data, root.right);
				}
			}
		} catch(Exception exc) {
			exc.printStackTrace();
		}
		return flag;
	}
	
	
}
