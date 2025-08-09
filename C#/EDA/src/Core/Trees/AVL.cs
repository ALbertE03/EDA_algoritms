using EDA.Core.NodeBinaryTree;
using EDA.Core.Interfaces;
namespace EDA.Core.AVL;

public class AVL<T> : IAVL<T> where T : IComparable<T>
{
    private NodeBinaryTree<T>? _root;

    public AVL()
    {
        _root = null;
    }

    public void Add(T item)
    {
        _root = AddRecursive(_root, item);
    }

    public void Delete(T item)
    {
        _root = DeleteRecursive(_root, item);
    }

    public NodeBinaryTree<T> Search(T item)
    {
        return SearchRecursive(_root, item);
    }

    public void Print(int lvl = 0)
    {
        _Print(_root, lvl);
    }
    


    #region privates
    private void _Print(NodeBinaryTree<T>? node, int lvl)
    {
        if (node == null)
        {
            return;
        }
        _Print(node.Left, lvl + 1);
        Console.WriteLine($"{new string(' ', lvl * 4)}[Nivel {lvl}] -> {node.Valor} (Altura: {node.Height})");
        _Print(node.Rigth, lvl + 1);
    }
    private NodeBinaryTree<T> SearchRecursive(NodeBinaryTree<T>? node, T item)
    {
        if (node == null || item.CompareTo(node.Valor) == 0)
            return node!;

        if (item.CompareTo(node.Valor) < 0)
            return SearchRecursive(node.Left, item);

        return SearchRecursive(node.Rigth, item);
    }


    private NodeBinaryTree<T>? DeleteRecursive(NodeBinaryTree<T>? node, T item)
    {
        if (node == null)
            return null;

        if (item.CompareTo(node.Valor) < 0)
        {
            node.Left = DeleteRecursive(node.Left, item);
        }
        else if (item.CompareTo(node.Valor) > 0)
        {
            node.Rigth = DeleteRecursive(node.Rigth, item);
        }
        else
        {
            if (node.Left == null)
                return node.Rigth;
            else if (node.Rigth == null)
                return node.Left;

            NodeBinaryTree<T> minRight = FindMin(node.Rigth);
            if (minRight.Valor != null)
            {
                node.Valor = minRight.Valor;
                node.Rigth = DeleteRecursive(node.Rigth, minRight.Valor);
            }
        }
        return Balance(node);
    }

    private NodeBinaryTree<T> AddRecursive(NodeBinaryTree<T>? node, T item)
    {
        if (node == null)
        {
            return new NodeBinaryTree<T>(item);
        }

        if (item.CompareTo(node.Valor) <= 0)
        {
            node.Left = AddRecursive(node.Left, item);
        }
        else if (item.CompareTo(node.Valor) > 0)
        {
            node.Rigth = AddRecursive(node.Rigth, item);
        }
        node.Height = GetHeight(node);
        return Balance(node);
    }

    private NodeBinaryTree<T> FindMin(NodeBinaryTree<T> node)
    {
        while (node.Left != null)
            node = node.Left;
        return node;
    }

    private NodeBinaryTree<T> Balance(NodeBinaryTree<T> node)
    {
        int balance = GetBalance(node);

        // Rotación  derecha
        if (balance > 1 && GetBalance(node.Left) >= 0)
            return RotateRight(node);

        // Rotación  izquierda  
        if (balance < -1 && GetBalance(node.Rigth) <= 0)
            return RotateLeft(node);

        // Rotación doble izquierda-derecha
        if (balance > 1 && GetBalance(node.Left) < 0)
        {
            node.Left = RotateLeft(node.Left!);
            return RotateRight(node);
        }

        // Rotación doble derecha-izquierda
        if (balance < -1 && GetBalance(node.Rigth) > 0)
        {
            node.Rigth = RotateRight(node.Rigth!);
            return RotateLeft(node);
        }

        return node;
    }

    private int GetHeight(NodeBinaryTree<T>? node)
    {
        if (node == null)
            return 0;
        return 1 + Math.Max(GetHeight(node.Left), GetHeight(node.Rigth));
    }

    private int GetBalance(NodeBinaryTree<T>? node)
    {
        if (node == null)
            return 0;
        return GetHeight(node.Left) - GetHeight(node.Rigth);
    }

    private NodeBinaryTree<T> RotateRight(NodeBinaryTree<T> y)
    {
        NodeBinaryTree<T> x = y.Left!;
        NodeBinaryTree<T>? T2 = x.Rigth;

        x.Rigth = y;
        y.Left = T2;
        x.Height = GetHeight(x);
        y.Height = GetHeight(y);
        return x;
    }

    private NodeBinaryTree<T> RotateLeft(NodeBinaryTree<T> x)
    {
        NodeBinaryTree<T> y = x.Rigth!;
        NodeBinaryTree<T>? T2 = y.Left;

        y.Left = x;
        x.Rigth = T2;
        x.Height = GetHeight(x);
        y.Height = GetHeight(y);
        return y;
    }


    #endregion
}