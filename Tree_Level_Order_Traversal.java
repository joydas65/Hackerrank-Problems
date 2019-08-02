public static void levelOrder(Node root) {
      
      Queue<Node> q = new LinkedList<>();
      q.add(root);
      while(q.size() > 0){
          Node nd = q.peek();
          if(nd.left != null)
            q.add(nd.left);
          if(nd.right != null)
            q.add(nd.right);
          System.out.print(nd.data+" ");
          q.poll();
      }
    }
