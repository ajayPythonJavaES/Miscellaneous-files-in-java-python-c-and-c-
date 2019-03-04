package com.java.multithreading;
/**
 * 
 * @author asarvasi: Stack using LinkedList
 *
 */
public class Stack extends LinkedList{
	
	private Node startNode, currNode;
	
	private static Stack stack;
	
	private int size = 0;
	
	public void add(int data) {
		try {
			Node newNode = null;
			newNode = new Node(data, null);
			if (size == 0) {
				startNode = currNode = newNode;
			} else if (currNode != null && size != 0) {
				currNode = currNode.next = newNode;
			}
			size++;
		} catch (Exception exc) {
			exc.printStackTrace();
		}
	}
	
	public void pop() {
		Node trav = startNode;
		Node prev = null;
		try {
			if(startNode == null)
				throw new Exception("Stack is empty");
			else {
				while(trav.next != null) {
					prev = trav;
					trav = trav.next;
				}
				prev.next = null;
				size--;
			}
		} catch(Exception exc) {
			exc.printStackTrace();
		}
	}
	
	public void displayData() {
		try {
			Node traceNext = startNode;
			if (size == 0) {
				throw new Exception("List is empty");
			} else {
				int i = 1;
				while (traceNext != null) {
					System.out.println(traceNext.data + "--" + i++);
					traceNext = traceNext.next;
				}
				System.out.println("Size of the list is: " + size);
			}
		} catch (Exception exc) {
			exc.printStackTrace();
		}
	}
	
	public static void main(String a[]) {
		stack = new Stack();
		stack.add(20);
		stack.add(30);
		stack.add(40);
		stack.pop();
		//stack.pop();
		stack.displayData();
	}
	
	
	
}
