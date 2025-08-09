using EDA.Core.MyList;
using System;
using EDA.Core.MyQueue;
using EDA.Core.MyStack;
using EDA.Core.AVL;
using EDA.Core.DisJoinSet;
namespace EDA
{
    class Program
    {
        public static void TestList()
        {
            Console.WriteLine("Testing My List");
            var list = new MyList<string>();
            list.Add("hola");
            list.Add("pepe");
            list.Add("sss");
            list.Print(); // hola -> pepe -> sss
            Console.WriteLine(list.Size); // 3
            list.Delete("pepe");
            list.Delete("hola");
            list.Print(); // sss
            Console.WriteLine(list.Size); // 1
            Console.WriteLine(list.isEmpty()); //false
            list.Delete("sss");
            Console.WriteLine(list.isEmpty()); //true
            list.Add("qwer");
            Console.WriteLine(list.Search("qwer")); // qwer
            Console.WriteLine();
        }
        public static void TestQueue()
        {
            Console.WriteLine("Testing My Queue");
            var cola = new MyQueue<int>();
            cola.Enqueue(2);
            cola.Enqueue(4);
            cola.Enqueue(24);
            cola.Enqueue(42);
            cola.Enqueue(21);
            cola.Enqueue(432);
            cola.Print(); //2 -> 4 -> 24 -> 42 -> 21 -> 432
            Console.WriteLine(cola.Peak()?.Value); // 2
            Console.WriteLine(cola.Peak()?.Value);//6
            Console.WriteLine(cola.isEmpty()); // false
            Console.WriteLine(cola.Peak()?.Value);//2
            Console.WriteLine(cola.Dequeue()?.Value);//2
            Console.WriteLine(cola.Peak()?.Value);//4
            Console.WriteLine(cola.Dequeue()?.Value);//4
            Console.WriteLine(cola.Dequeue()?.Value);//24
            Console.WriteLine(cola.Dequeue()?.Value);//42
            Console.WriteLine(cola.Dequeue()?.Value);//21
            Console.WriteLine(cola.Dequeue()?.Value);//432
            Console.WriteLine(cola.Size); // 0 
            try
            {
                Console.WriteLine(cola.Dequeue()?.Value); // error
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message); //Cola vacia
            }
            Console.WriteLine(cola.isEmpty()); //true
           
            Console.WriteLine();

        }
        public static void TestStack()
        {
            Console.WriteLine("Testing My Stack");
            var pila = new MyStack<int>();
            pila.Add(2);
            pila.Add(22);
            pila.Add(23);
            pila.Print(); //[23,22,2]
            Console.WriteLine(pila.pop().Value);//23
            Console.WriteLine(pila.pop().Value);//22
            Console.WriteLine();
        }

        public static void TestAVL()
        {
            Console.WriteLine("Testing My AVL");
            var avl = new AVL<int>();
            avl.Add(2);
            avl.Add(5);
            avl.Add(6);
            avl.Add(6);
            avl.Add(6);
            avl.Add(1);
            avl.Add(0);
            avl.Add(-1);
            avl.Add(-2);
            avl.Print();
            /* 
            salida
            5
          /  \
        1     6 
       / \   /   \
    -1    2 6     6    
    / \
   -2  0
            */
            Console.WriteLine(avl.Search(1).Valor);//1
            avl.Delete(1);
            Console.WriteLine();
            avl.Print();
                        /* 
                salida
                5
               /  \
             -1     6 
             / \   /  \
           -2   0 6     6    
           
         
                */
            
            
            if(avl.Search(1)?.Valor==null){
                 Console.WriteLine("null");//null
            }else{
                throw new Exception("No deberia estar aqui nunca");
            }
           

            var avl2 = new AVL<string>();
            avl2.Add("Hola");
            avl2.Add("Pepe");
            avl2.Add("Jose");
            avl2.Add("Albert");
            Console.WriteLine();
            avl2.Print();
            /*
            Jose
           /    \
        Hola    Pepe
        /
      Albert  
            */
            avl2.Delete("Hola");
            Console.WriteLine();
            avl2.Print();
               /*
            Jose
           /    \
        Albert    Pepe 
            */
            Console.WriteLine();
        }

        public static void TestDisJoinSet()
        {
            Console.WriteLine("Testing DisjointSet with integers:");
            var ds = new DisJoinSet<int>();
            
            ds.merge(1, 0);
            ds.merge(2, 0);
            ds.merge(4, 3);
            ds.merge(5, 3);
            
            Console.WriteLine($"Find(0): {ds.find(0)}"); // 0 (raíz del conjunto {0,1,2})
            Console.WriteLine($"Find(1): {ds.find(1)}"); // 0 (mismo conjunto que 0)
            Console.WriteLine($"Find(2): {ds.find(2)}"); // 0 (mismo conjunto que 0)
            Console.WriteLine($"Find(3): {ds.find(3)}"); // 3 (raíz del conjunto {3,4,5})
            Console.WriteLine($"Find(4): {ds.find(4)}"); // 3 (mismo conjunto que 3)
            Console.WriteLine($"Find(22): {ds.find(22)}"); // 22 (nuevo conjunto {22})
            
            Console.WriteLine($"¿Están conectados 1 y 2? {ds.is_connected(1, 2)}"); // true
            Console.WriteLine($"¿Están conectados 1 y 4? {ds.is_connected(1, 4)}"); // false
            Console.WriteLine($"¿Están conectados 4 y 5? {ds.is_connected(4, 5)}"); // true
            
            ds.merge(1, 4);
            Console.WriteLine($"Después de merge(1, 4):");
            Console.WriteLine($"¿Están conectados 1 y 4? {ds.is_connected(1, 4)}"); // true
            Console.WriteLine($"¿Están conectados 2 y 5? {ds.is_connected(2, 5)}"); // true
            
            // Test con número de conjuntos
            Console.WriteLine($"Número de conjuntos: {ds.GetNumberOfSets()}"); // 2 ({0,1,2,3,4,5} y {22})
            
            Console.WriteLine("\nTesting DisjointSet with strings:");
            var dsString = new DisJoinSet<string>();
            dsString.merge("Alice", "Bob");
            dsString.merge("Charlie", "David");
            dsString.merge("Eve", "Frank");
            dsString.merge("Bob", "Charlie");
            
            Console.WriteLine($"¿Están conectados Alice y David? {dsString.is_connected("Alice", "David")}"); // true
            Console.WriteLine($"¿Están conectados Alice y Eve? {dsString.is_connected("Alice", "Eve")}"); // false
            Console.WriteLine($"Número de conjuntos de strings: {dsString.GetNumberOfSets()}"); // 2
            
            Console.WriteLine($"Miembros del conjunto de Alice: [{string.Join(", ", dsString.GetSetMembers("Alice"))}]");
            Console.WriteLine();
        }
        static void Main(String[] args)
        {
            //TestList();
            //TestQueue();
            //TestStack();
            //TestAVL();
            TestDisJoinSet();
        }
    }
        
}