package com.java.multithreading;

/**
 * 
 * @author asarvasi This linked list is implemented without using array.
 */

class Node {
	int data;
	Node next;

	public Node(int data, Node next) {
		this.data = data;
		this.next = next;
	}

}

public class LinkedList {

	private int size = 0;

	private Node currNode, startNode;

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

	public void delete(int data) {
		try {
			Node trav = startNode;
			Node prev = null;

			while (trav != null) {
				if (trav.data == data) {
					if (prev != null) {
						prev.next = trav.next;
					} else {
						startNode = trav.next;
					}
					size--;
				} else {
					prev = trav;
				}
				trav = trav.next;
			}

		} catch (Exception exc) {
			exc.printStackTrace();
		}
	}

	public static void main(String ar[]) {
		LinkedList llObj = new LinkedList();
		int i = 10;
		while (i != 0) {
			llObj.add(i * 10);
			--i;
		}
		llObj.displayData();
		llObj.delete(10);
		llObj.displayData();
	}

}
