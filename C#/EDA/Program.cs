using EDA.Core.MyList;
using System;
using EDA.Core.MyQueue;
using EDA.Core.MyStack;


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
        }
        static void Main(String[] args)
        {
            TestList();
            TestQueue();
            TestStack();

        }
    }
        
}