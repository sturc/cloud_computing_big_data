import java.io.IOException;
import java.util.Iterator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class NasaPageCountByDomain {

   public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
      private static final IntWritable one = new IntWritable(1);
      private Text word = new Text();
      private Pattern siteExp = Pattern.compile("\\..*\\,\\d*\\,GET\\,");
   
      public void map(Object key, Text value, Context context) 
                  throws IOException, InterruptedException {
         Matcher matcher = this.siteExp.matcher(value.toString());
         if (matcher.find()) {
            String line = value.toString().substring(matcher.start(), matcher.end());
            String urlString = line.substring(0, line.indexOf(","));
            int pointIndex = urlString.lastIndexOf(".");
            this.word.set(urlString.substring(pointIndex >= 0 ? pointIndex : 0));
            context.write(this.word, one);
         }
   
      }
   }

   public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
      private IntWritable result = new IntWritable();
   
      public void reduce(Text key, Iterable<IntWritable> values, Context context) 
                        throws IOException, InterruptedException {
         int sum = 0;
   
         IntWritable currValue;
         for(Iterator iter = values.iterator(); iter.hasNext(); sum += currValue.get()) {
            currValue = (IntWritable)iter.next();
         }
   
         this.result.set(sum);
         context.write(key, this.result);
      }
   }

   public static void main(String[] var0) throws Exception {
      Configuration var1 = new Configuration();
      Job var2 = Job.getInstance(var1, "Page Count by Domain");
      var2.setJarByClass(NasaPageCountByDomain.class);
      var2.setMapperClass(NasaPageCountByDomain.TokenizerMapper.class);
      var2.setCombinerClass(NasaPageCountByDomain.IntSumReducer.class);
      var2.setReducerClass(NasaPageCountByDomain.IntSumReducer.class);
      var2.setOutputKeyClass(Text.class);
      var2.setOutputValueClass(IntWritable.class);
      FileInputFormat.addInputPath(var2, new Path(var0[0]));
      FileOutputFormat.setOutputPath(var2, new Path(var0[1]));
      System.exit(var2.waitForCompletion(true) ? 0 : 1);
   }
}
