using System;
using CoreEscuela.Entidades;

namespace Etapa1
{
    class Program
    {
        static void Main(string[] args)
        {
            //invoca al constructor.
            var escuela = new Escuela("Platzi .NET Dojo", 2021);
            escuela.Pais = "Colombia";
            escuela.Ciudad = "Bogota";
            escuela.TipoEscuela = TiposEscuela.Primaria;

            //asigno nombre

            /*    Console.WriteLine(escuela.Nombre);
               Console.WriteLine(escuela.AñoDeCreación); */
            Console.WriteLine(escuela);
        }
    }
}