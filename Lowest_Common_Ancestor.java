import java.util.*;
import java.io.*;

class Node {
    Node left;
    Node right;
    int data;
    
    Node(int data) {
        this.data = data;
        left = null;
        right = null;
    }
}

class Solution {

	/*
    class Node 
    	int data;
    	Node left;
    	Node right;
	*/

    public static ArrayList<Node> insertNodes(ArrayList<Node> n, Node root, int v){
        /*if(root.data == v){
            n.add(root);
            return n;
        }*/
        while(root.data != v){
            if(root.data < v){
                n.add(root);
                root = root.right;
            }
            else if(root.data > v){
                n.add(root);
                root = root.left;
            }   
        }
        n.add(root);
        return n;
    }


	public static Node lca(Node root, int v1, int v2) {


        ArrayList<Node> n1 = new ArrayList<Node>();
        ArrayList<Node> n2 = new ArrayList<Node>();

      	// Write your code here.
        n1 = insertNodes(n1,root,v1);
        n2 = insertNodes(n2,root,v2);
        ArrayList<Node> arr = new ArrayList<Node>();
        int i = 0;
        for(Node item : n1){
            if(n2.contains(item)){
                arr.add(item);
                i += 1;
            }
        }
        return arr.get(i-1);
    }

	public static Node insert(Node root, int data) {
        if(root == null) {
            return new Node(data);
        } else {
            Node cur;
            if(data <= root.data) {
                cur = insert(root.left, data);
                root.left = cur;
            } else {
                cur = insert(root.right, data);
                root.right = cur;
            }
            return root;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt();
        Node root = null;
        while(t-- > 0) {
            int data = scan.nextInt();
            root = insert(root, data);
        }
      	int v1 = scan.nextInt();
      	int v2 = scan.nextInt();
        scan.close();
        Node ans = lca(root,v1,v2);
        System.out.println(ans.data);
    }	
}
