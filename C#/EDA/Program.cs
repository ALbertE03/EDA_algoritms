using EDA.Core.MyList;
using System;
using EDA.Core.MyQueue;


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
            Console.WriteLine(cola.Peak()?.Value); // 2
            Console.WriteLine(cola.isEmpty()); // false
            Console.WriteLine(cola.Peak()?.Value);//2
            Console.WriteLine(cola.Dequeue()?.Value);//2
            Console.WriteLine(cola.Peak()?.Value);//4
            Console.WriteLine(cola.Dequeue()?.Value);//4
            Console.WriteLine(cola.Dequeue()?.Value);//24
            Console.WriteLine(cola.Dequeue()?.Value);//42
            Console.WriteLine(cola.Dequeue()?.Value);//21
            Console.WriteLine(cola.Dequeue()?.Value);//432
            try
            {
                Console.WriteLine(cola.Dequeue()?.Value);//2
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message); //Cola vacia
            }
            Console.WriteLine(cola.isEmpty()); //true
           

        }
        static void Main(String[] args)
        {
            TestList();
            TestQueue();
            
    }
        }
        
}