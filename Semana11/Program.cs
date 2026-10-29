using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Semana11 {
    internal class Program {
        static void Main(string[] args) {
            ejer6();
        }

        static void ejer1() {
            int[] num = new int[5];

            for(int i = 0; i < num.Length; i++) {
                Console.Write($"Ingrese el número {i + 1}: ");
                num[i] = int.Parse(Console.ReadLine());
                Console.Clear();
            }

            Console.WriteLine("\nNúmeros ingresados:");
            foreach (int i in num)
                Console.WriteLine(i);
        }

        static void ejer2() {
            int[] num = { -2, 5, -1, 0, 8, -6, 3 };

            Console.WriteLine("Números originales:");
            foreach (int i in num)
                Console.WriteLine(i);

            Console.WriteLine("\nNúmeros reemplazados:");
            for (int i = 0;i < num.Length; i++) {
                if (num[i] < 0)
                    num[i] = 0;
                Console.WriteLine(num[i]);
            }   
        }
        static void ejer3() {
            int[] num = { 10, 50, 6, 3, 7, 20 };

            Console.WriteLine("Números originales:");
            foreach (int i in num)
                Console.WriteLine(i);

            int minimo = num[0];
            int maximo = num[0];

            for(int i =1; i < num.Length; i++) {
                if(num[i] < minimo)
                    minimo = num[i];
                if(num[i] > maximo) 
                    maximo = num[i];
            }
            Console.WriteLine("\nMinimo: "+ minimo);
            Console.WriteLine("Máximo: "+maximo);
        }

        static void ejer4() {
            int[] num = new int[10];

            for (int i = 0; i < num.Length; i++) {
                Console.Write($"Ingrese el número {i + 1}: ");
                num[i] = int.Parse(Console.ReadLine());
                Console.Clear();
            }

            Console.WriteLine("Números ingresados:");
            foreach (int i in num)
                Console.Write(i+" ");

            Console.WriteLine("\n\nLista de números pares: ");
            for(int i = 0; i < num.Length; i++) {
                if (num[i]%2==0)
                    Console.Write(num[i] + " ");
            }
            Console.ReadKey();
        }

        static void ejer5() {
            Console.Write("Ingrese la cantidad de números a registrar: ");
            int c = int.Parse(Console.ReadLine());
            Console.Clear();

            int[] num = new int[c];
            int suma = 0;

            for (int i = 0;i < num.Length; i++) {
                Console.Write($"Ingrese número {i + 1}: ");
                num[i] = int.Parse(Console.ReadLine()) ;
                suma += num[i];
                Console.Clear();
            }

            Console.WriteLine("\nNúmeros ingresados:");
            foreach (int i in num)
                Console.Write(i + " ");

            Console.WriteLine("\n\nSuma de todos números: " + suma);
            Console.ReadKey();
        }

        static void ejer6() {
            string[] pro = new string[5];
            int r = 0;

            for(int i = 0; r < pro.Length; i++) {
                Console.Write($"Ingrese producto {r + 1}: ");
                string nuevo = Console.ReadLine();
                bool duplicado = false;

                for( int j = 0; j < pro.Length; j++) {
                    if( pro[j] == nuevo) {
                        Console.WriteLine("Producto duplicado.!\n");
                        duplicado = true;
                        break;
                    }
                }

                if (!duplicado) {
                    pro[r] = nuevo;
                    r++;
                }
            }
            Console.WriteLine("\nProductos registrados:");
            foreach (string i in pro)
                Console.WriteLine(i);
        }
    }
}
