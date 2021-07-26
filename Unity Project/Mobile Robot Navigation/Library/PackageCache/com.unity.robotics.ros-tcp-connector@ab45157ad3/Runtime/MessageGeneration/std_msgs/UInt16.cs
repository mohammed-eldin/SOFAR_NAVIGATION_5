//Do not edit! This file was generated by Unity-ROS MessageGeneration.
using System;
using System.Linq;
using System.Collections.Generic;
using System.Text;
using RosMessageGeneration;

namespace RosMessageTypes.Std
{
    public class UInt16 : Message
    {
        public const string RosMessageName = "std_msgs/UInt16";

        public ushort data;

        public UInt16()
        {
            this.data = 0;
        }

        public UInt16(ushort data)
        {
            this.data = data;
        }
        public override List<byte[]> SerializationStatements()
        {
            var listOfSerializations = new List<byte[]>();
            listOfSerializations.Add(BitConverter.GetBytes(this.data));

            return listOfSerializations;
        }

        public override int Deserialize(byte[] data, int offset)
        {
            this.data = BitConverter.ToUInt16(data, offset);
            offset += 2;

            return offset;
        }

        public override string ToString()
        {
            return "UInt16: " +
            "\ndata: " + data.ToString();
        }
    }
}
