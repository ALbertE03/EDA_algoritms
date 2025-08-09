using EDA.Core.Interfaces;
using System;
namespace EDA.Core.DisJoinSet;

public class DisJoinSet<T> : IDisJoinSet<T> where T : notnull
{
    private Dictionary<T, T> parent;
    private Dictionary<T, int> rank;

    public DisJoinSet()
    {
        parent = new Dictionary<T, T>();
        rank = new Dictionary<T, int>();
    }

    public void MakeSet(T item)
    {
        if (!parent.ContainsKey(item))
        {
            parent[item] = item;
            rank[item] = 0;
        }
    }

    public T find(T item)
    {
        if (!parent.ContainsKey(item))
        {
            MakeSet(item);
            return item;
        }

        if (!parent[item].Equals(item))
        {
            parent[item] = find(parent[item]);
        }
        return parent[item];
    }

    public void merge(T x, T y)
    {
        T rootX = find(x);
        T rootY = find(y);
        
        if (rootX.Equals(rootY)) 
            return;

        if (rank[rootX] < rank[rootY])
        {
            parent[rootX] = rootY;
        }
        else if (rank[rootX] > rank[rootY])
        {
            parent[rootY] = rootX;
        }
        else
        {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }

    public bool is_connected(T x, T y)
    {
        return find(x).Equals(find(y));
    }

    public int GetNumberOfSets()
    {
        var roots = new HashSet<T>();
        foreach (var item in parent.Keys)
        {
            roots.Add(find(item));
        }
        return roots.Count;
    }

    public IEnumerable<T> GetSetMembers(T item)
    {
        T root = find(item);
        return parent.Keys.Where(key => find(key).Equals(root));
    }
}