package com.ds.plugin;

public class LinkedListUsingArrays {

	class Node {
		Object data;
		Node node;

		Node(Object data, Node node) {
			this.data = data;
			this.node = node;
		}
	}

	private Node[] list;
	private int currentPos;
	private static int DEFAULT_CAPACITY = 10;
	private int size = 0;

	public LinkedListUsingArrays() {
		try {
			list = new Node[DEFAULT_CAPACITY];
			currentPos = 0;
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
	}

	private LinkedListUsingArrays(int capacity) {
		try {
			list = new Node[capacity];
			currentPos = 0;
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
	}

	public void push(Object data) {
		try {
			Node dataNode = new Node(data, null);

			if (currentPos > DEFAULT_CAPACITY) {
				CheckCapacity ccObj = new CheckCapacity(currentPos);
				ccObj.start();
			}

			if (currentPos == 0) {
				list[currentPos] = dataNode;
			} else {
				list[currentPos] = list[currentPos - 1].node = dataNode;
			}
			currentPos++;
			size++;
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
	}

	public void pop() {
		try {
			if (currentPos == 0) {
				throw new LinkedListException("List is empty");
			} else {
				currentPos--;
				size--;
				list[currentPos] = list[currentPos - 1].node = null;
			}
		} catch (LinkedListException eMsg) {
			eMsg.printStackTrace();
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
	}

	public int size() {
		return size;
	}

	public int getIndex(Object data) {
		int pos = 0;
		try {
			boolean flag = false;
			int loop = 0;
			for (Node node : list) {
				if (node != null && node.data.equals(data)) {
					flag = true;
					pos = loop;
				}
				loop++;
			}
			if (!flag) {
				pos = -1;
			}
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
		return pos;
	}

	public void displayElements() {
		try {
			Node headNode = list[0];
			if (headNode == null) {
				throw new LinkedListException("List is empty");
			} else {
				while (headNode != null) {
					System.out.println(headNode.data);
					headNode = headNode.node;
				}
			}

		} catch (LinkedListException lleMsg) {
			lleMsg.printStackTrace();
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
	}

	class CheckCapacity extends Thread {

		private int _size;

		private CheckCapacity(int _size) {
			this._size = _size;
		}

		@Override
		public void run() {
			try {
				if (_size > Integer.MAX_VALUE) {
					throw new LinkedListException("Stack overflow");
				} else {
					if (_size > DEFAULT_CAPACITY) {
						DEFAULT_CAPACITY *= 3 / 2;
						@SuppressWarnings("unused")
						LinkedListUsingArrays llObj = new LinkedListUsingArrays(
								DEFAULT_CAPACITY);
					}
				}
			} catch (LinkedListException eMsg) {
				eMsg.printStackTrace();
			}
		}

	}

}
