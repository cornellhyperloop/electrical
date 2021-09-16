using System;
using System.Threading;

using VectorNav.Sensor;

class Program
{
	static void Main(string[] args)
	{
		const string SensorPort = "COM5";
		const UInt32 SensorBaudrate = 115200;

		var ez = EzAsyncData.Connect(SensorPort, SensorBaudrate);
        bool problem;

        while(true)
        {
            if (ez.CurrentData.HasYawPitchRoll)
            {
                var cdPrev = ez.CurrentData.YawPitchRoll;

                // Delay
                Thread.Sleep(500);

                var cdCurr = ez.CurrentData.YawPitchRoll;

                problem = Math.Abs(cdCurr.Z - cdPrev.Z) >= 45 || Math.Abs(cdCurr.Y - cdPrev.Y) >= 45 || Math.Abs(cdCurr.X - cdPrev.X) >= 60;

                if (problem) Console.WriteLine("Problem");
                Console.WriteLine("No Problem");
            }
        }

		ez.Disconnect();
	}

}
