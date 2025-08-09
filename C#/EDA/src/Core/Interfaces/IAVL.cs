using System.Dynamic;
using EDA.Core.NodeBinaryTree;
namespace EDA.Core.Interfaces
{
    public interface IAVL<T> where T : IComparable<T>
    {
        void Delete(T item);
        void Add(T item);
        NodeBinaryTree<T> Search(T item);
        void Print(int l);
    }
}