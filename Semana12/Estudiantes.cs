using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana12 {
    internal class Estudiantes {
        byte[] edades = new byte[0];
        int cant = 0;

        public void registrar() {
            byte ed;
            do {
                Console.Write("\nIngrese la edad del estudiante: ");
                if (byte.TryParse(Console.ReadLine(), out ed) && ed >= 14 && ed <= 120) break;
                else Console.WriteLine("Error. Ingrese una edad entre 14 y 120.");
            } while (true);

            Array.Resize(ref edades, edades.Length+1);
            edades[cant] = ed;
            cant++;

            Console.WriteLine("\nEdad ingresado con exito!");
        }

        public void mostrar() {
            Console.WriteLine("\nPOS\tEDADES");
            for(int i = 0; i < edades.Length; i++) {
                Console.WriteLine(i+"\t"+edades[i]);
            }
        }
    }
}
