using System;
using System.ComponentModel.DataAnnotations;

namespace QuotingDojo.Models
{
    public class Quote
    {
        [Key]
        public int id { get; set; }

        [Required]
        public string author { get; set; }

        [Required]
        public string content { get; set; }

        public DateTime created_at { get; set; } = DateTime.Now;
        public DateTime updated_at { get; set; } = DateTime.Now;
    }
}