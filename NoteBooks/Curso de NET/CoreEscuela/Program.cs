using System;

namespace CoreEscuela
{
    class CoreEscuela
    {
        public string nombre;
        public string direccion;
        public int añoFundacion;

        public string unicoEstudiante;

        public void Timbrar()
        {
            //Todo
            Console.Beep(987, 1000); //Si
            Console.Beep(1174, 500); //Re'
            Console.Beep(880, 1500); //La

            Console.Beep(783, 250); //Sol
            Console.Beep(880, 250); //La
            Console.Beep(987, 1000); //Si

            Console.Beep(1174, 500); //Re'
            Console.Beep(880, 1500); //La

            Console.Beep(987, 1000); //Si
            Console.Beep(1174, 500); //Re'
            Console.Beep(1760, 1000); //La'
            Console.Beep(1567, 500); //Sol'
            Console.Beep(1174, 1000); //Re'

            Console.Beep(1046, 250); //Do
            Console.Beep(987, 250); //Si
            Console.Beep(880, 1000); //La

            Console.Beep(523, 500); //Do;
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            var miEscuela = new CoreEscuela();
            Console.WriteLine("Modelando escuela con Core!");
            miEscuela.nombre = "UNIVERSIDAD DEL INSONMNIO CON .NET";
            miEscuela.direccion = "alejandro.chem.io@gmail.com";
            miEscuela.unicoEstudiante = "Alejandro Giraldo Londoño";
            miEscuela.añoFundacion = 1990;
            Console.WriteLine("TONADA!");
            miEscuela.Timbrar();
            miEscuela.Timbrar();
        }
    }
}
