## Contents

- [Visual Transformers on Cats and dogs dataset](#visual-transformers-on-cats-and-dogs-dataset)
- [Training logs](#training-logs)
- [Visual Transformers](#visual-transformers)
- [References](#references) 



### Visual Transformers on Cats and dogs dataset

Implementing visual transformer on the Cat & Dog dataset as given in this [blog](https://analyticsindiamag.com/hands-on-vision-transformers-with-pytorch/). The dataset is obtained from [Kaggle](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data). 

- Dataset view

![image](https://user-images.githubusercontent.com/47082769/128538664-311c378d-66fa-4a99-ac0b-3003e7de0243.png)



### Training logs

Model is trained for 20 epochs & can be viewed here in the [jupyter_notebook](https://github.com/karthikmohan1702/EVA6/blob/main/S13_VisionTransformers%20/S13_VIT_Dog_Cat.ipynb)

Showing last 5 training log 

    Epoch : 15 - loss : 0.6071 - acc: 0.6598 - val_loss : 0.6114 - val_acc: 0.6559

    100%
    313/313 [02:14<00:00, 2.33it/s]

    Epoch : 16 - loss : 0.6025 - acc: 0.6694 - val_loss : 0.6060 - val_acc: 0.6659

    100%
    313/313 [01:50<00:00, 2.84it/s]

    Epoch : 17 - loss : 0.5951 - acc: 0.6750 - val_loss : 0.6011 - val_acc: 0.6669

    100%
    313/313 [04:30<00:00, 1.16it/s]

    Epoch : 18 - loss : 0.5968 - acc: 0.6723 - val_loss : 0.6048 - val_acc: 0.6644

    100%
    313/313 [02:15<00:00, 2.31it/s]

    Epoch : 19 - loss : 0.5915 - acc: 0.6792 - val_loss : 0.5947 - val_acc: 0.6826

    100%
    313/313 [01:48<00:00, 2.88it/s]

    Epoch : 20 - loss : 0.5937 - acc: 0.6739 - val_loss : 0.5924 - val_acc: 0.6839

### Visual Transformers

- Transformer encoder

![image](https://user-images.githubusercontent.com/47082769/128548386-85c8e224-e5a1-4dce-830c-a34b32c04aa9.png)


Transformers are a evolution in the computer vision. They are designed for text or NLP world, but vision transformer are designed to replace the CNN operations. In NLP we pass tokens as inputs to the transformer since these inputs will be in the sequence whereas in vision space, we pass patches from an image.
for eg: if we have a batch of image which is of shape (32-batchsize, 3-channels, 224-height, 224-width) & projection here is the a 2D convolution operation and feeding our batch of images to projection leads to - (32, 768, 14, 14) & then we flatten the image using flatten function. 

    class PatchEmbeddings(nn.Module):
        """
        Image to Patch Embedding.

        """

        def __init__(self, image_size=224, patch_size=16, num_channels=3, embed_dim=768):
            super().__init__()
            image_size = to_2tuple(image_size)
            patch_size = to_2tuple(patch_size)
            num_patches = (image_size[1] // patch_size[1]) * (image_size[0] // patch_size[0])
            self.image_size = image_size
            self.patch_size = patch_size
            self.num_patches = num_patches

            self.projection = nn.Conv2d(num_channels, embed_dim, kernel_size=patch_size, stride=patch_size)

        def forward(self, pixel_values):
            batch_size, num_channels, height, width = pixel_values.shape
            # FIXME look at relaxing size constraints
            if height != self.image_size[0] or width != self.image_size[1]:
                raise ValueError(
                    f"Input image size ({height}*{width}) doesn't match model ({self.image_size[0]}*{self.image_size[1]})."
                )
            x = self.projection(pixel_values).flatten(2).transpose(1, 2)
            return x

Here in the below class creates embeddings which then can feeded to ViT, we are creating positional information of the patches of the images as a positional embedding along with the patch embedding from the Patch embedding class. A learnable class parameter is also passed such that for each sequence & position of the image, the class is assigned which helps in prediction of the input image.

    class ViTEmbeddings(nn.Module):
        """
        Construct the CLS token, position and patch embeddings.

        """

        def __init__(self, config):
            super().__init__()

            self.cls_token = nn.Parameter(torch.zeros(1, 1, config.hidden_size))
            self.patch_embeddings = PatchEmbeddings(
                image_size=config.image_size,
                patch_size=config.patch_size,
                num_channels=config.num_channels,
                embed_dim=config.hidden_size,
            )
            num_patches = self.patch_embeddings.num_patches
            self.position_embeddings = nn.Parameter(torch.zeros(1, num_patches + 1, config.hidden_size))
            self.dropout = nn.Dropout(config.hidden_dropout_prob)

        def forward(self, pixel_values):
            batch_size = pixel_values.shape[0]
            embeddings = self.patch_embeddings(pixel_values)

            cls_tokens = self.cls_token.expand(batch_size, -1, -1)
            embeddings = torch.cat((cls_tokens, embeddings), dim=1)
            embeddings = embeddings + self.position_embeddings
            embeddings = self.dropout(embeddings)
            return embeddings

Next we ned to have the config for the VIT, which contains all the config elements (like - num of hidden layers, intermediate size, attention prob, hidden dropout, num of channels, image size & other hyperparameters) that is needed to run Vision transformer.

    class ViTConfig():
      def __init__(
            self,
            hidden_size=768,
            num_hidden_layers=12,
            num_attention_heads=12,
            intermediate_size=3072,
            hidden_act="gelu",
            hidden_dropout_prob=0.0,
            attention_probs_dropout_prob=0.0,
            initializer_range=0.02,
            layer_norm_eps=1e-12,
            is_encoder_decoder=False,
            image_size=224,
            patch_size=16,
            num_channels=3,
            **kwargs
        ):

            self.hidden_size = hidden_size
            self.num_hidden_layers = num_hidden_layers
            self.num_attention_heads = num_attention_heads
            self.intermediate_size = intermediate_size
            self.hidden_act = hidden_act
            self.hidden_dropout_prob = hidden_dropout_prob
            self.attention_probs_dropout_prob = attention_probs_dropout_prob
            self.initializer_range = initializer_range
            self.layer_norm_eps = layer_norm_eps

            self.image_size = image_size
            self.patch_size = patch_size
            self.num_channels = num_channels
            


    class ViTSelfAttention(nn.Module):
        def __init__(self, config):
            super().__init__()
            if config.hidden_size % config.num_attention_heads != 0 and not hasattr(config, "embedding_size"):
                raise ValueError(
                    f"The hidden size {config.hidden_size,} is not a multiple of the number of attention "
                    f"heads {config.num_attention_heads}."
                )

            self.num_attention_heads = config.num_attention_heads
            self.attention_head_size = int(config.hidden_size / config.num_attention_heads)
            self.all_head_size = self.num_attention_heads * self.attention_head_size

            self.query = nn.Linear(config.hidden_size, self.all_head_size)
            self.key = nn.Linear(config.hidden_size, self.all_head_size)
            self.value = nn.Linear(config.hidden_size, self.all_head_size)

            self.dropout = nn.Dropout(config.attention_probs_dropout_prob)

        def transpose_for_scores(self, x):
            new_x_shape = x.size()[:-1] + (self.num_attention_heads, self.attention_head_size)
            x = x.view(*new_x_shape)
            return x.permute(0, 2, 1, 3)

        def forward(self, hidden_states, head_mask=None, output_attentions=False):
            mixed_query_layer = self.query(hidden_states)

            key_layer = self.transpose_for_scores(self.key(hidden_states))
            value_layer = self.transpose_for_scores(self.value(hidden_states))
            query_layer = self.transpose_for_scores(mixed_query_layer)

            # Take the dot product between "query" and "key" to get the raw attention scores.
            attention_scores = torch.matmul(query_layer, key_layer.transpose(-1, -2))

            attention_scores = attention_scores / math.sqrt(self.attention_head_size)

            # Normalize the attention scores to probabilities.
            attention_probs = nn.Softmax(dim=-1)(attention_scores)

            # This is actually dropping out entire tokens to attend to, which might
            # seem a bit unusual, but is taken from the original Transformer paper.
            attention_probs = self.dropout(attention_probs)

            # Mask heads if we want to
            if head_mask is not None:
                attention_probs = attention_probs * head_mask

            context_layer = torch.matmul(attention_probs, value_layer)

            context_layer = context_layer.permute(0, 2, 1, 3).contiguous()
            new_context_layer_shape = context_layer.size()[:-2] + (self.all_head_size,)
            context_layer = context_layer.view(*new_context_layer_shape)

            outputs = (context_layer, attention_probs) if output_attentions else (context_layer,)

            return outputs
            
Below is a simple class which adds the dropout.

    class ViTSelfOutput(nn.Module):
      """
      This is just a Linear Layer Block
      """
      def __init__(self, config):
        super().__init__()
        self.dense = nn.Linear(config.hidden_size, config.hidden_size)
        self.dropout = nn.Dropout(config.hidden_dropout_prob)

      def forward(self, hidden_states, input_tensor):
        hidden_states = self.dense(hidden_states)
        hidden_states = self.dropout(hidden_states)

        return hidden_states
        
        
    class ViTAttention(nn.Module):
        def __init__(self, config):
            super().__init__()
            self.attention = ViTSelfAttention(config)
            self.output = ViTSelfOutput(config)
            self.pruned_heads = set()

        def prune_heads(self, heads):
            if len(heads) == 0:
                return
            heads, index = find_pruneable_heads_and_indices(
                heads, self.attention.num_attention_heads, self.attention.attention_head_size, self.pruned_heads
            )

            # Prune linear layers
            self.attention.query = prune_linear_layer(self.attention.query, index)
            self.attention.key = prune_linear_layer(self.attention.key, index)
            self.attention.value = prune_linear_layer(self.attention.value, index)
            self.output.dense = prune_linear_layer(self.output.dense, index, dim=1)

            # Update hyper params and store pruned heads
            self.attention.num_attention_heads = self.attention.num_attention_heads - len(heads)
            self.attention.all_head_size = self.attention.attention_head_size * self.attention.num_attention_heads
            self.pruned_heads = self.pruned_heads.union(heads)

        def forward(self, hidden_states, head_mask=None, output_attentions=False):
            self_outputs = self.attention(hidden_states, head_mask, output_attentions)

            attention_output = self.output(self_outputs[0], hidden_states)

            outputs = (attention_output,) + self_outputs[1:]  # add attentions if we output them
            return outputs        



### References

- https://analyticsindiamag.com/hands-on-vision-transformers-with-pytorch/
- https://www.kaggle.com/general/74235 
- https://www.analyticsvidhya.com/blog/2021/03/an-image-is-worth-16x16-words-transformers-for-image-recognition-at-scale-vision-transformers/
