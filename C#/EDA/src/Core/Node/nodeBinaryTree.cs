using System.ComponentModel;

namespace EDA.Core.NodeBinaryTree;


public class NodeBinaryTree<T>
{
    public NodeBinaryTree<T>? Rigth { get; set; }
    public NodeBinaryTree<T>? Left { get; set; }
    public int Height { get; set; }
    public T? Valor;
    public NodeBinaryTree(T? valor)
    {
        Valor = valor;
        Rigth = null;
        Left = null;
        Height = 1;

    }
}