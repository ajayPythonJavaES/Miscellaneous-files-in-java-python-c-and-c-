package com.java.multithreading;


class Table<K,V> {
	
	final K key;
	V value;
	Table<K,V> next;
	
	Table(K key, V value, Table<K,V> next) {
		this.key = key;
		this.value = value;
		this.next = next;
	}
	
	public final K getKey() {
		return key;
	}
	
	public final V getValue() {
		return value;
	}
	
	
}


public class Dictionary {

	
	
	
}
