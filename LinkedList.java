package com.plugin.ds;

public class LinkedList {

	private static final long serialVersionUID = 1L;

	private static Object[] store;
	private final int DEFAULT_CAPACITY = 10;
	
	private static int size = 0;
	
	private static int currentPos = 0;
	
	public LinkedList() {
		store = new Object[DEFAULT_CAPACITY];
	}
	
	public LinkedList(int capacity) {
		store = new Object[capacity];
	}
	
	private class Node {
		
		Object data = null;
		Node node = null;
		
		Node(Object data, Node node) {
			this.data = data;
			this.node = node;
		}
	}
	
	public boolean push(Object data) {
		Node head = null;
		if(store[currentPos] != null) {
			head = (Node)store[currentPos];
		}
		return false;
	}
	
	
}
