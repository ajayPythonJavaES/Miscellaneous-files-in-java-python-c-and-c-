package com.ds.plugin;

public class LinkedList {

	class Node {
		Object data;
		Node node;

		Node() {

		}
	}

	private Node[] list;
	private int currentPos;
	private static int DEFAULT_CAPACITY = 10;

	public LinkedList() {
		try {
			list = new Node[DEFAULT_CAPACITY];
			currentPos = 0;
		} catch (Exception eMsg) {
			eMsg.printStackTrace();
		}
	}

	private void push(Object data) {
		try {
			if (currentPos != 0) {
				Node prevNode = list[currentPos];

				Node dataNode = new Node();
				dataNode.data = data;
				dataNode.node = null;

				if (prevNode != null && prevNode.node == null) {
					prevNode.node = dataNode;
				}
			}
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
					}
				}
			} catch (LinkedListException eMsg) {

			}
		}

	}

}
