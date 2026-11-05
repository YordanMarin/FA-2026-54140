using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana12 {
    internal class Program {
        static void Main(string[] args) {
            Estudiantes est = new Estudiantes();
            string conti;
            int opc;
            do {
                Console.WriteLine("BIENVENIDOS AL SISTEMA DE REGISTRO DE EDADES\n");
                Console.WriteLine("0. Salir");
                Console.WriteLine("1. Insertar");
                Console.WriteLine("2. Mostrar");
                Console.WriteLine("3. Eliminar");
                Console.WriteLine("4. Ordenar\n");

                do {
                    Console.Write("Ingrese una opción: ");
                    if (int.TryParse(Console.ReadLine(), out opc) && opc >=0 && opc <=4) break;
                    else Console.WriteLine("Error. Ingrese un número del 1 al 4.\n");
                } while (true);

                switch (opc) {
                    case 0:Environment.Exit(0); break;
                    case 1:est.registrar(); break;
                    case 2:est.mostrar(); break;
                    case 3:break;
                    case 4:break;
                }

                do {
                    Console.Write("\n¿Desea regresar al menú? [Si/No]: ");
                    conti = Console.ReadLine().ToLower().Trim();

                    if (conti != "si" && conti != "no") Console.WriteLine("Error. Ingrese solo si o no.");

                } while (conti != "si" && conti != "no");
                Console.Clear();
            } while (conti =="si");
        }
    }
}
