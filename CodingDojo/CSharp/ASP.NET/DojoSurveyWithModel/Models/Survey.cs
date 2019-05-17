using System.ComponentModel.DataAnnotations;

namespace DojoSurveyWithModel.Models
{
    public class Survey
    {
        [Required(ErrorMessage = "Please enter a name")]
        [MinLength(2, ErrorMessage = "Name needs to be at least 2 characters")]
        public string Name { get; set; }

        [Required(ErrorMessage = "Select A Location")]
        public string Location { get; set; }

        [Required(ErrorMessage = "Select A Favorite Language")]
        public string Language { get; set; }

        [MinLength(20, ErrorMessage = "Comment needs to be at least 20 characters")]      
        public string Textarea { get; set; }
    }
}