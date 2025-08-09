
namespace EDA.Core.Interfaces
{
    public interface IDisJoinSet<T>
    {
        T? find(T item);
        void merge(T x, T y);
        bool is_connected(T x, T y);
    }
    
}