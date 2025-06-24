Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

using System;
using System.Collections.Generic;

class Curso
{
    public List<string> Asignaturas { get; set; }

    public Curso()
    {
        Asignaturas = new List<string>();
    }

    public void MostrarAsignaturas()
    {
        Console.WriteLine("Asignaturas del curso:");
        foreach (var asignatura in Asignaturas)
        {
            Console.WriteLine("- " + asignatura);
        }
    }
}

class Program
{
    static void Main()
    {
        Curso curso = new Curso();
        curso.Asignaturas.AddRange(new string[] { "Matemáticas", "Física", "Química", "Historia", "Lengua" });
        curso.MostrarAsignaturas();
    }
}

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

using System;
using System.Collections.Generic;

class Curso
{
    public List<string> Asignaturas { get; set; }

    public Curso()
    {
        Asignaturas = new List<string>();
    }

    public void MostrarAsignaturas()
    {
        foreach (var asignatura in Asignaturas)
        {
            Console.WriteLine($"Yo estudio {asignatura}");
        }
    }
}

class Program
{
    static void Main()
    {
        Curso curso = new Curso();
        curso.Asignaturas.AddRange(new string[] { "Matemáticas", "Física", "Química", "Historia", "Lengua" });

        curso.MostrarAsignaturas();
    }
}

Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

using System;
using System.Collections.Generic;

class Loteria
{
    public List<int> NumerosGanadores { get; private set; }

    public Loteria()
    {
        NumerosGanadores = new List<int>();
    }

    public void PedirNumeros(int cantidad)
    {
        Console.WriteLine($"Ingrese {cantidad} números ganadores de la lotería primitiva:");

        while (NumerosGanadores.Count < cantidad)
        {
            Console.Write($"Número {NumerosGanadores.Count + 1}: ");
            string input = Console.ReadLine();

            if (int.TryParse(input, out int numero))
            {
                if (numero < 1 || numero > 49)
                {
                    Console.WriteLine("El número debe estar entre 1 y 49. Intente nuevamente.");
                }
                else if (NumerosGanadores.Contains(numero))
                {
                    Console.WriteLine("Número repetido. Ingrese otro diferente.");
                }
                else
                {
                    NumerosGanadores.Add(numero);
                }
            }
            else
            {
                Console.WriteLine("Entrada inválida. Ingrese un número válido.");
            }
        }
    }

    public void MostrarNumerosOrdenados()
    {
        NumerosGanadores.Sort();
        Console.WriteLine("Números ganadores ordenados de menor a mayor:");

        foreach (int num in NumerosGanadores)
        {
            Console.Write(num + " ");
        }
        Console.WriteLine();
    }
}

class Program
{
    static void Main()
    {
        Loteria loteria = new Loteria();
        int cantidadNumeros = 6; // Número típico en lotería primitiva

        loteria.PedirNumeros(cantidadNumeros);
        loteria.MostrarNumerosOrdenados();
    }
}

Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

using System;
using System.Collections.Generic;

class Numeros
{
    public List<int> ListaNumeros { get; private set; }

    public Numeros()
    {
        ListaNumeros = new List<int>();
    }

    public void LlenarLista()
    {
        for (int i = 1; i <= 10; i++)
        {
            ListaNumeros.Add(i);
        }
    }

    public void MostrarInverso()
    {
        ListaNumeros.Reverse();
        Console.WriteLine(string.Join(", ", ListaNumeros));
    }
}

class Program
{
    static void Main()
    {
        Numeros numeros = new Numeros();
        numeros.LlenarLista();
        numeros.MostrarInverso();
    }
}

Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

using System;
using System.Collections.Generic;

class Abecedario
{
    public List<char> Letras { get; private set; }

    public Abecedario()
    {
        Letras = new List<char>();
    }

    public void LlenarAbecedario()
    {
        for (char c = 'A'; c <= 'Z'; c++)
        {
            Letras.Add(c);
        }
    }

    public void EliminarMultiplosDeTres()
    {
        // Consideramos posiciones empezando en 1 para el usuario
        // Eliminamos letras en posiciones múltiplos de 3 (3, 6, 9, ...)
        // Para no afectar los índices al eliminar, creamos una lista temporal

        List<char> resultado = new List<char>();

        for (int i = 0; i < Letras.Count; i++)
        {
            int posicion = i + 1; // posiciones 1-based
            if (posicion % 3 != 0)
            {
                resultado.Add(Letras[i]);
            }
        }

        Letras = resultado;
    }

    public void MostrarLetras()
    {
        Console.WriteLine("Letras restantes:");
        Console.WriteLine(string.Join(", ", Letras));
    }
}

class Program
{
    static void Main()
    {
        Abecedario abecedario = new Abecedario();
        abecedario.LlenarAbecedario();
        abecedario.EliminarMultiplosDeTres();
        abecedario.MostrarLetras();
    }
}

